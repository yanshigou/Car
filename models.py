# 为数据库导出

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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
    user = models.ForeignKey('Users', models.DO_NOTHING)
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Carinfo'


class Cart(models.Model):
    brand = models.CharField(max_length=30)
    picture = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    newprice = models.CharField(max_length=30)
    mileage = models.CharField(max_length=30)
    car = models.ForeignKey(Carinfo, models.DO_NOTHING)
    suser = models.ForeignKey('Users', models.DO_NOTHING)

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
    buy_user = models.ForeignKey('Users', models.DO_NOTHING)
    sale_user = models.ForeignKey('Users', models.DO_NOTHING)
    isdelete = models.IntegerField(db_column='isDelete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'


class Users(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    cellphone = models.CharField(max_length=11)
    realname = models.CharField(max_length=50)
    uidentity = models.CharField(max_length=18)
    address = models.CharField(max_length=150)
    sex = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Users'


class UsersGroups(models.Model):
    userinfo = models.ForeignKey(Users, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Users_groups'
        unique_together = (('userinfo', 'group'),)


class UsersUserPermissions(models.Model):
    userinfo = models.ForeignKey(Users, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Users_user_permissions'
        unique_together = (('userinfo', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
