from django.db import models
#from django.forms import ValidationError
from django.core.exceptions import ValidationError
# Create your models here

def check_for_a(value):
    if value[0].lower()=='a':
        raise ValidationError('started with a')



class Topic(models.Model):
    topic_name=models.CharField(max_length=100,validators=[check_for_a])

    def __str__(self):
        return self.topic_name