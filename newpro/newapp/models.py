from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=30)
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    department = models.CharField(max_length=30)



