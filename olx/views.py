from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'elon': 41324})
