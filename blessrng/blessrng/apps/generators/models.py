from django.db import models

# Create your models here.


class RandIntSet(models.Model):
    floor = models.IntegerField('floor')
    ceiling = models.IntegerField('ceiling')
    length = models.IntegerField('length')
    generated_at = models.DateTimeField('date published')


class RandInt(models.Model):
    set_id = models.ForeignKey(
        RandIntSet, on_delete=models.CASCADE)
    value = models.IntegerField('value')


class RandPwdSet(models.Model):
    length = models.IntegerField('length')
    pwd_length = models.IntegerField('pwd_length')
    generated_at = models.DateTimeField('generated_at')


class RandPwd(models.Model):
    set_id = models.ForeignKey(
        RandPwdSet, on_delete=models.CASCADE)
    value = models.CharField('value', max_length=128)
