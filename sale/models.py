from django.db import models
from userinfo.models import Users

# Create your models here.
class Brand(models.Model):
    logo_brand = models.CharField(max_length=100)
    btitle = models.CharField(max_length=30)
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Brand'


class Carinfo(models.Model):
    ctitle = models.CharField(max_length=30)
    regist_date = models.DateField()
    engineno = models.CharField(db_column='engineNo', max_length=30)  # Field name made lowercase.
    mileage = models.IntegerField()
    maintenance_record = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    extractprice = models.DecimalField(max_digits=8, decimal_places=2)
    newprice = models.DecimalField(max_digits=8, decimal_places=2)
    picture = models.CharField(max_length=100)
    formalities = models.CharField(max_length=10)
    debt = models.CharField(max_length=10)
    promise = models.TextField(blank=True, null=True)
    examine = models.CharField(max_length=30)
    ispurchase = models.IntegerField(db_column='isPurchase')  # Field name made lowercase.
    serbran = models.ForeignKey(Brand, models.DO_NOTHING)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Carinfo'