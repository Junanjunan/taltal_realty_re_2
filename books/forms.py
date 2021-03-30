from django import forms
from . import models


class RoomLeaseForm(forms.ModelForm):
    class Meta:
        model = models.RoomLease
        """fields = (
            'realtor',
            'address',
            "deposit",
            "month_fee",
            "management_fee",
            "area_m2",
            "room",
            "bath",
            "owner_phone",
            "tenant_phone",
            "parking",
            "elevator",
            "loan",
            "empty",
            "naver",
            "not_finished",
            "finished",
            "description")"""
        """"fields = '__all__'"""
        exclude = ['realtor']


class RoomDealingForm(forms.ModelForm):
    class Meta:
        model = models.RoomDealing
        fields = ('address',
                  'price',
                  "deposit",
                  "month_fee",
                  "management_fee",
                  "area_m2",
                  "room",
                  "bath",
                  "owner_phone",
                  "tenant_phone",
                  "parking",
                  "elevator",
                  "empty",
                  "naver",
                  "not_finished",
                  "finished",
                  "description")


class StoreLeaseForm(forms.ModelForm):
    class Meta:
        model = models.StoreLease
        fields = ('address',
                  'right_deposit',
                  "deposit",
                  "month_fee",
                  "management_fee",
                  "area_m2",
                  "owner_phone",
                  "tenant_phone",
                  "parking",
                  "elevator",
                  "empty",
                  "naver",
                  "not_finished",
                  "finished",
                  "description")


class BuildingDealingForm(forms.ModelForm):
    class Meta:
        model = models.BuildingDealing
        fields = ('address',
                  'price',
                  'equity',
                  "deposit",
                  "month_fee",
                  "land_m2",
                  'land_type',
                  "owner_phone",
                  "elevator",
                  "naver",
                  "not_finished",
                  "finished",
                  "description")
