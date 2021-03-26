from django import forms
from . import models


class HouseLeaseCustomerForm(forms.ModelForm):
    class Meta:
        model = models.HouseLeaseCustomer
        fields = (
            "guest_phone",
            "deposit",
            "month_fee",
            "room",
            "area_m2",
            "description",
            "not_finished",
            "finished",
        )


class HouseDealingCustomerForm(forms.ModelForm):
    class Meta:
        model = models.HouseDealingCustomer
        fields = (
            "guest_phone",
            "price",
            "room",
            "area_m2",
            "parking",
            "elevator",
            "description",
            "not_finished",
            "finished",
        )


class ShopLeaseCustomerForm(forms.ModelForm):
    class Meta:
        model = models.ShopLeaseCustomer
        fields = (
            "guest_phone",
            "deposit",
            "month_fee",
            "area_m2",
            "description",
            "not_finished",
            "finished",
        )


class BuildingDealingCustomerForm(forms.ModelForm):
    class Meta:
        model = models.BuildingDealingCustomer
        fields = (
            "guest_phone",
            "price",
            "description",
            "elevator",
            "not_finished",
            "finished",
        )
