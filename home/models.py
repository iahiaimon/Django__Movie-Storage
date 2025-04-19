from django.db import models
from django.contrib.auth.models import User , AbstractUser 

# Create your models here.

class CustomUser(AbstractUser):
    # name = models.CharField(max_length=100 , null=False , blank=False)
    # email = models.EmailField(max_length=100 , null=False , blank=False , unique=True)
    phone_number = models.CharField(max_length=15 , null=False , blank=False)
    # password = models.CharField(max_length=100 , null=False , blank=False)
    # conform_password = models.CharField(max_length=100 , null=False , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} -- {self.email}"
    

