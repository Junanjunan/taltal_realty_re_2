from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from . import models


@admin.register(models.HouseLeaseCustomer)
class HouseLeaseCustomerAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = (
        "guest_phone",
        "updated",
        "deposit",
        "month_fee",
        "room",
        "area_m2",
        "not_finished",
        "finished",
        "description",
    )


@admin.register(models.ShopLeaseCustomer)
class ShopLeaseCustomerAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = (
        "guest_phone",
        "updated",
        "deposit",
        "month_fee",
        "area_m2",
        "not_finished",
        "finished",
        "description",
    )


@admin.register(models.HouseDealingCustomer)
class HouseDealingCustomerAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = (
        "guest_phone",
        "updated",
        "price",
        "room",
        "area_m2",
        "not_finished",
        "finished",
        "description",
    )


@admin.register(models.BuildingDealingCustomer)
class BuildingDealingCustomerAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = (
        "guest_phone",
        "updated",
        "price",
        "elevator",
        "not_finished",
        "finished",
        "description",
    )