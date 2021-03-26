from django.urls import path
from . import views as contract_views 

app_name = 'contracts'

urlpatterns = [
    path("contracts/", contract_views.ContractView.as_view(), name='contracts')
]