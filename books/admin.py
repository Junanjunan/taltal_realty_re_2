from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from . import models


@admin.register(models.RoomLease)
class RoomLeaseAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = (
        "address",
        "updated",
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
        "description"
    )


@admin.register(models.RoomDealing)
class RoomDealingAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = (
        "address",
        "updated",
        "price",
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
        "description"
    )


@admin.register(models.StoreLease)
class StoreLeaseAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = (
        "address",
        "updated",
        "right_deposit",
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
        "description"
    )


@admin.register(models.BuildingDealing)
class BuildingDealingAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = (
        'address',
        'updated',
        'price',
        'equity',
        'deposit',
        'month_fee',
        'land_m2',
        'land_type',
        'owner_phone',
        'elevator',
        'naver',
        'not_finished',
        'finished',
        'description'
    )
