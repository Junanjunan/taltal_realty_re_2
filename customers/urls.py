from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
    path("houselease/", views.HouseLeaseCustomerList.as_view(), name="house-lease-customer-list"),
    path("houselease/<int:pk>/", views.HouseLeaseCustomerDeatil.as_view(), name="house-lease-customer-detail"),
    path("houselease/creating/", views.HouseLeaseCustomerCreating.as_view(), name="house-lease-customer-creating"),
    path("houselease/<int:pk>/update/", views.HouseLeaseCustomerUpdate.as_view, name="house-lease-customer-update"),
    path("houselease/search/", views.houselease_customer_search, name="house-lease-customer-search"),
    path("houselease/<int:pk>/delete/", views.houselease_customer_delete, name="house-lease-customer-delete"),
    path("shoplease/", views.ShopLeaseCustomerList.as_view(), name="shop-lease-customer-list"),
    path("shoplease/<int:pk>/", views.ShopLeaseCustomerDeatil.as_view(), name="shop-lease-customer-detail"),
    path("shoplease/creating/", views.ShopLeaseCustomerCreating.as_view(), name="shop-lease-customer-creating"),
    path("shoplease/<int:pk>/update/", views.ShopLeaseCustomerUpdate.as_view, name="shop-lease-customer-update"),
    path("shoplease/search/", views.shoplease_customer_search, name="shop-lease-customer-search"),
    path("shoplease/<int:pk>/delete/", views.shoplease_customer_delete, name="shop-lease-customer-delete"),
    path("housedealing/", views.HouseDealingCustomerList.as_view(), name="house-dealing-customer-list"),
    path("housedealing/<int:pk>/", views.HouseDealingCustomerDeatil.as_view(), name="house-dealing-customer-detail"),
    path("housedealing/creating/", views.HouseDealingCustomerCreating.as_view(), name="house-dealing-customer-creating"),
    path("housedealing/<int:pk>/update/", views.HouseDealingCustomerUpdate.as_view, name="house-dealing-customer-update"),
    path("housedealing/search/", views.housedealing_customer_search, name="house-dealing-customer-search"),
    path("housedealing/<int:pk>/delete/", views.housedealing_customer_delete, name="house-dealing-customer-delete"),
    path("buildingdealing/", views.BuildingDealingCustomerList.as_view(), name="building-dealing-customer-list"),
    path("buildingdealing/<int:pk>/", views.BuildingDealingCustomerDeatil.as_view(), name="building-dealing-customer-detail"),
    path("buildingdealing/creating/", views.BuildingDealingCustomerCreating.as_view(), name="building-dealing-customer-creating"),
    path("buildingdealing/<int:pk>/update/", views.BuildingDealingCustomerUpdate.as_view, name="building-dealing-customer-update"),
    path("buildingdealing/search/", views.buildingdealing_customer_search, name="building-dealing-customer-search"),
    path("buildingdealing/<int:pk>/delete/", views.buildingdealing_customer_delete, name="building-dealing-customer-delete"),
]