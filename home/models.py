from django.db import models
from django.contrib.auth.models import User , AbstractUser 

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15 , null=False , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} -- {self.email}"
    


class AddMovie(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True)
    catagory = models.CharField(max_length=200 , null=False , blank=False)
    publish = models.DateField()
    image = models.ImageField(upload_to='movie_images', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # userid = models.ForeignKey(CustomUser , null=False , on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title} -- {self.userid}"

    


