from pickle import TRUE
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

# User model
class User(models.Model):
    id = models.AutoField(primary_key=TRUE)
    name = models.CharField(max_length=50)
    # Tuples are used to store multiple items in a single variable.
    type = models.CharField(max_length=100,choices=(('student','student'),('teacher','teacher')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)