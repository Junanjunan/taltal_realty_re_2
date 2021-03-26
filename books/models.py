from django.db import models


class RoomLease(models.Model):

    address = models.CharField(max_length=200)
    updated = models.DateField(auto_now=True)
    deposit = models.IntegerField(default=0)
    month_fee = models.IntegerField(default=0)
    management_fee = models.IntegerField(default=0)
    area_m2 = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    bath = models.IntegerField(default=0)
    owner_phone = models.CharField(max_length=200)
    tenant_phone = models.CharField(max_length=200)
    parking = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    loan = models.BooleanField(default=False)
    empty = models.BooleanField(default=False)
    naver = models.BooleanField(default=False)
    not_finished = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    description = models.TextField(default=False)


class RoomDealing(models.Model):

    address = models.CharField(max_length=200)
    updated = models.DateField(auto_now=True)
    price = models.IntegerField()
    deposit = models.IntegerField(default=0)
    month_fee = models.IntegerField(default=0)
    management_fee = models.IntegerField(default=0)
    area_m2 = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    bath = models.IntegerField(default=0)
    owner_phone = models.CharField(max_length=200)
    tenant_phone = models.CharField(max_length=200)
    parking = models.BooleanField()
    elevator = models.BooleanField()
    empty = models.BooleanField()
    naver = models.BooleanField()
    not_finished = models.BooleanField(default=True)
    finished = models.BooleanField()
    description = models.TextField()


"""below store"""


class StoreLease(models.Model):

    address = models.CharField(max_length=200)
    updated = models.DateField(auto_now=True)
    right_deposit = models.IntegerField(default=0)
    deposit = models.IntegerField(default=0)
    month_fee = models.IntegerField(default=0)
    management_fee = models.IntegerField(default=0)
    area_m2 = models.IntegerField(default=0)
    owner_phone = models.CharField(max_length=200)
    tenant_phone = models.CharField(max_length=200)
    parking = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    empty = models.BooleanField(default=False)
    naver = models.BooleanField(default=False)
    not_finished = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    description = models.TextField(default=False)


"""below building"""


class BuildingDealing(models.Model):

    address = models.CharField(max_length=200)
    updated = models.DateField(auto_now=True)
    price = models.IntegerField()
    equity = models.IntegerField(default=0)
    deposit = models.IntegerField(default=0)
    month_fee = models.IntegerField(default=0)
    land_m2 = models.IntegerField(default=0)
    land_type = models.CharField(max_length=15)
    owner_phone = models.CharField(max_length=200)
    elevator = models.BooleanField()
    naver = models.BooleanField()
    not_finished = models.BooleanField(default=True)
    finished = models.BooleanField()
    description = models.TextField()


