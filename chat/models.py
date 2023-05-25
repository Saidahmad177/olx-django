from datetime import datetime
from django.db import models
from users.models import CustomUser


class Room(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender_user')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver_user')

    def __str__(self):
        return f"{self.sender} and {self.receiver}"


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.room.sender} and {self.room.receiver}"

