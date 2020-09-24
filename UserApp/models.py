from django.db import models


# Create your models here.
class User(models.Model):
    phonenum = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    birthday = models.CharField(max_length=32)
    avatar = models.CharField(max_length=32)
    location = models.CharField(max_length=32)

    class Meta:
        db_table = 'user'
