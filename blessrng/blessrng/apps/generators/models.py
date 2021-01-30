from django.db import models

# Create your models here.



class Random_Int_Sequence(models.Model):
    floor = models.IntegerField('floor')
    ceiling = models.IntegerField('ceiling')
    sequence_Length = models.IntegerField('length')
    generated_at = models.DateTimeField('date published')



class Random_Int(models.Model):
    sequence_id = models.ForeignKey(Random_Int_Sequence, on_delete=models.CASCADE)
    value = models.IntegerField('value')


class Random_Password_Sequence(models.Model):
    sequence_Length = models.IntegerField('length')
    generated_at = models.DateTimeField('date published')



class Random_Password(models.Model):
    sequence_id = models.ForeignKey(Random_Password_Sequence, on_delete=models.CASCADE)
    generated_Password = models.CharField('value',max_length = 128 )