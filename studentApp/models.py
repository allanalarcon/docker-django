from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    test_score = models.FloatField()

class Course(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    instructor = models.CharField(max_length=20)
    rating = models.FloatField()
    price = models.FloatField()