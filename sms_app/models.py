from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True) 
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# Create your models here.
