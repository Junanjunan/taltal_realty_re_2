from django.db import models


class Contract(models.Model):
    """ Contract Custom Model """

    address = models.CharField(max_length=100)
    contract_day = models.DateField()
    last_day = models.DateField()
