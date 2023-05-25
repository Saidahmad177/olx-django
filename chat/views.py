from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from chat.models import Message, Room
from django.http import HttpResponse, JsonResponse

from users.models import CustomUser


@login_required
def home(request):
    users = CustomUser.objects.all()
    user_in_room = []
    user_in_room2 = []
    exists_user = 0

    if Room.objects.filter(sender=request.user):
        user_in_room = Room.objects.filter(sender=request.user)
        exists_user = 1

    if Room.objects.filter(receiver=request.user):
        user_in_room2 = Room.objects.filter(receiver=request.user)
        exists_user = 1

    context = {
        'users': users,
        'user_in_room': user_in_room,
        'user_in_room2': user_in_room2,
        'exists_user': exists_user,
    }

    return render(request, 'chat/home.html', context)

@login_required
def room2(request, receiver_id):
    username = request.user.username
    room_details = Room.objects.get(id=receiver_id)
    print(room_details, 'room-details-----------')
    user_in_room = []
    user_in_room2 = []

    if Room.objects.filter(sender=request.user):
        user_in_room = Room.objects.filter(sender=request.user)

    if Room.objects.filter(receiver=request.user):
        user_in_room2 = Room.objects.filter(receiver=request.user)

    context = {
        'user_in_room': user_in_room,
        'user_in_room2': user_in_room2,
        'username': username,
        'receiver_id': receiver_id,
        'room_details': room_details,
    }

    return render(request, 'chat/room2.html', context)

@login_required
def checkview2(request, receiver_id):
    receiver = CustomUser.objects.get(id=receiver_id)
    print(receiver, 'receiver')
    print(receiver.id, 'number')

    if Room.objects.filter(sender=request.user, receiver=receiver_id).exists():
        room_id = Room.objects.get(sender=request.user, receiver=receiver_id)
        print(room_id.id, 'rooooooooooooooooooom')
        print(True, 'True')
        return redirect(reverse('room2', kwargs={'receiver_id': room_id.id}))

    elif Room.objects.filter(receiver=request.user, sender=receiver_id).exists():
        room_id = Room.objects.get(receiver=request.user, sender=receiver_id)
        return redirect(reverse('room2', kwargs={'receiver_id': room_id.id}))

    else:
        print(False, 'False')
        new_room = Room.objects.create(
            sender=request.user,
            receiver=receiver,
        )
        new_room.save()
        return redirect(reverse('room2', kwargs={'receiver_id': new_room.id}))

@login_required
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    user = CustomUser.objects.get(username=username)
    room = Room.objects.get(id=room_id)

    new_message = Message.objects.create(
        user=user,
        value=message,
        room=room,
    )
    new_message.save()
    return HttpResponse('Message sent successfully')

@login_required
def getMessages2(request, receiver_id):
    room = Room.objects.get(id=receiver_id)
    messages = Message.objects.filter(room=room).select_related('user')
    message_list = []
    for message in messages:
        message_dict = {
            'username': message.user.username,
            'value': message.value,
            'date': message.date.strftime('%Y-%m-%d %H:%M'),
        }
        message_list.append(message_dict)
    return JsonResponse({"messages": message_list})
