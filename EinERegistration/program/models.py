from django.db import models

# Create your models here.


class Program(models.Model):
    name = models.CharField(max_length=250)
    level = models.IntegerField()
    prerequisite = models.CharField(max_length=250)
    description = models.TextField()


class Iteration(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    region = models.CharField(max_length=2)
    jk = models.CharField(max_length=100)
    facilitator = models.CharField(max_length=250)

