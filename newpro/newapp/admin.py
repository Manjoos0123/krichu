from django.contrib import admin
from . models import Student
admin.site.register(Student)
from . models import Teacher
admin.site.register(Teacher)

# Register your models here.
