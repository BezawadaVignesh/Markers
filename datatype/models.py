from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=100)
    sender_email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'Sender: {self.sender}, Email: {self.sender_email}, message: {self.message}, Date: {self.date}'