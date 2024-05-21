from django.contrib.auth.models import User
from django.db import models



# Create your models here.


class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20)

    def __str__(self):

        return self.name
    

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email=models.EmailField(blank=True)
   


    def __str__(self):
        return str(self.user)