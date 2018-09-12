from django.db import models
from userinfo.models import Users
from sale.models import Carinfo
# Create your models here.
class Cart(models.Model):
    brand = models.CharField(max_length=30)
    picture = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    newprice = models.CharField(max_length=30)
    mileage = models.CharField(max_length=30)
    car = models.ForeignKey(Carinfo, models.DO_NOTHING)
    suser = models.ForeignKey(Users, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Cart'


class Orders(models.Model):
    brand = models.CharField(max_length=30)
    picture = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    newprice = models.CharField(max_length=30)
    mileage = models.CharField(max_length=30)
    orderno = models.CharField(db_column='orderNo', max_length=30)  # Field name made lowercase.
    orderstatus = models.IntegerField(db_column='orderStatus')  # Field name made lowercase.
    buy_user = models.ForeignKey(Users, models.DO_NOTHING, related_name='buy_user_id')
    sale_user = models.ForeignKey(Users, models.DO_NOTHING, related_name='sale_user_id')
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'