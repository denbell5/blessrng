from django.db import models

# Create your models here.



class Generated_Value(models.Model):
    value = models.IntegerField('value')
    generated_at = models.DateTimeField('date published')