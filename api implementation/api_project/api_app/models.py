from django.db import models


class Student(models.Model):
          studentID = models.IntegerField()
          name = models.CharField(max_length=255)
          grade = models.CharField(max_length=50)
          address = models.CharField(max_length=100)
