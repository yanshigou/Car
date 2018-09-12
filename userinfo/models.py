from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Users(AbstractUser):
    cellphone = models.CharField(max_length=11)
    realname = models.CharField(max_length=50)
    uidentity = models.CharField(max_length=18)
    address = models.CharField(max_length=150)
    sex = models.CharField(max_length=10)

    class Meta:
        managed = False  # 意思为不需要再同步回数据库
        db_table = 'Users'
        verbose_name = '用户'