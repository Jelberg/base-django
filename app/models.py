from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Vote for {self.choice} in {self.poll}"