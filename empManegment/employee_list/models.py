from django.db import models

# Create your models here.

class Position(models.Model):
        title = models.CharField(max_length=20)


class Employee(models.Model):
    fullname = models.CharField(max_length=20)
    emp_code = models.CharField(max_length=2)
    phone = models.CharField(max_length=11 )
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
