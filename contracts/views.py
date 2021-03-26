from django.views.generic import View, ListView
from django.shortcuts import render
from . import models


class ContractView(ListView):

    model = models.Contract



# def contract_object(request):
#     return render(request, "contracts/contract.html")