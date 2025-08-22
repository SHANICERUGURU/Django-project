from django.db import models
from cloudinary.models import CloudinaryField
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Subscriber(models.Model): 
    email= models.EmailField(unique=True)   
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class Pet(models.Model):
    name=models.CharField(max_length=30) 
    description=models.TextField()
    pet_image= CloudinaryField('image', null= True)
# Create your models here.
