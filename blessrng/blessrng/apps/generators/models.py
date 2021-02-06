from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BaseSet(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    generated_at = models.DateTimeField()
    count = models.IntegerField()

    class Meta:
        abstract = True


class RandIntSet(BaseSet):
    floor = models.IntegerField()
    ceiling = models.IntegerField()
    values = ArrayField(models.IntegerField())


class RandPwdSet(BaseSet):
    pwd_length = models.IntegerField()
    values = ArrayField(models.CharField(max_length=64))


class RandWordSet(BaseSet):
    all_text = models.CharField(max_length=32768)
    word_length = models.IntegerField()
    values = ArrayField(models.CharField(max_length=1024))
