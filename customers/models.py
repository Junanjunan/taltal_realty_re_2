from django.db import models

"""below customer"""

class HouseLeaseCustomer(models.Model):

    guest_phone = models.CharField(max_length=30)
    updated = models.DateField(auto_now=True)
    deposit = models.IntegerField(default=0)
    month_fee = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    area_m2 = models.IntegerField(default=0)
    parking = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    loan = models.BooleanField(default=False)
    not_finished = models.BooleanField(default=True)
    finished = models.BooleanField()
    description = models.TextField()


class ShopLeaseCustomer(models.Model):
    
    guest_phone = models.CharField(max_length=30)
    updated = models.DateField(auto_now=True)
    deposit = models.IntegerField(default=0)
    month_fee = models.IntegerField(default=0)
    area_m2 = models.IntegerField(default=0)
    parking = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    not_finished = models.BooleanField(default=True)
    finished = models.BooleanField()
    description = models.TextField()
    

class HouseDealingCustomer(models.Model):

    guest_phone = models.CharField(max_length=30)
    updated = models.DateField(auto_now=True)
    price = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    area_m2 = models.IntegerField(default=0)
    parking = models.BooleanField()
    elevator = models.BooleanField()
    not_finished = models.BooleanField(default=True)
    finished = models.BooleanField()
    description = models.TextField()


class BuildingDealingCustomer(models.Model):

    guest_phone = models.CharField(max_length=30)
    updated = models.DateField(auto_now=True)
    price = models.IntegerField(default=0)
    elevator = models.BooleanField()
    not_finished = models.BooleanField(default=True)
    finished = models.BooleanField()
    description = models.TextField()