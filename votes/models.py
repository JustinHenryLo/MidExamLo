from django.db import models
from datetime import datetime

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    birthdate = models.DateTimeField(default=datetime.now ,blank=True)
    platform = models.TextField()


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    vote_datetime = models.DateTimeField( auto_now=True)

