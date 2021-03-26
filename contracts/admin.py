from django.contrib import admin
from . import models


@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Basic Info', {'fields':('address', 'contract_day', 'last_day')},
        ),
    )

    list_display = ('address', 'contract_day', 'last_day')