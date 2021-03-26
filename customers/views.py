from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from . import models, forms


class HouseLeaseCustomerList(ListView):
    model = models.HouseLeaseCustomer
    context_object_name = 'houselease_customers'
    template_name = 'customers/houselease/houselease_list.html'


class HouseLeaseCustomerDeatil(DetailView):
    model = models.HouseLeaseCustomer
    template_name = 'customers/houselease/houselease_detail.html'


class HouseLeaseCustomerCreating(CreateView):
    form_class = forms.HouseLeaseCustomerForm
    template_name = 'customers/houselease/houselease_creating.html'

    def form_valid(self, form):
        form.save()
        return redirect(reverse("customers:house-lease-customer-list"))


class HouseLeaseCustomerUpdate(UpdateView):
    model = models.HouseLeaseCustomer
    template_name = "customers/houselease/houselease_update.html"
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

    def form_valid(self, form):
        form.save()
        return redirect(reverse("customers:house-lease-customer-list"))


def houselease_customer_search(request):

    deposit = int(request.GET.get("deposit", 0))
    month_fee = int(request.GET.get("month_fee", 0))
    room = request.GET.get("room", 0)
    area_m2 = int(request.GET.get("area_m2", 0))
    parking = request.GET.get("parking")
    elevator = request.GET.get("elevator")
    loan = request.GET.get("loan")
    not_finished = request.GET.get("not_finished")
    finished = request.GET.get("finished")
   
    filter_args = {}
    filter_args["deposit__lte"] = deposit
    filter_args["month_fee__lte"] = month_fee
    filter_args["area_m2__gte"] = area_m2
    filter_args["room__contains"] = room
    if parking == "on":
        filter_args["parking"] = True
    if elevator == "on":
        filter_args["elevator"] = True
    if loan == "on":
        filter_args["loan"] = True
    if not_finished == "on":
        filter_args["not_finished"] = True
    if finished == "on":
        filter_args["finished"] = True
    houselease_customers = models.HouseLeaseCustomer.objects.filter(**filter_args)
    return render(request, "customers/houselease/houselease_search.html", {**filter_args, "houselease_customers": houselease_customers})


def houselease_customer_delete(request, pk):
    houselease_customer = models.HouseLeaseCustomer.objects.filter(pk=pk).delete()
    return redirect(reverse("customers:house-lease-customer-list"))

"""below shoplease"""


class ShopLeaseCustomerList(ListView):
    model = models.ShopLeaseCustomer
    context_object_name = 'shoplease_customers'
    template_name = 'customers/shoplease/shoplease_list.html'


class ShopLeaseCustomerDeatil(DetailView):
    model = models.ShopLeaseCustomer
    template_name = 'customers/shoplease/shoplease_detail.html'


class ShopLeaseCustomerCreating(CreateView):
    form_class = forms.ShopLeaseCustomerForm
    template_name = 'customers/shoplease/shoplease_creating.html'

    def form_valid(self, form):
        form.save()
        return redirect(reverse("customers:shop-lease-customer-list"))


class ShopLeaseCustomerUpdate(UpdateView):
    model = models.ShopLeaseCustomer
    template_name = "customers/shoplease/shoplease_update.html"
    fields = (
        "guest_phone",
        "updated",
        "deposit",
        "month_fee",
        "area_m2",
        "parking",
        "elevator",
        "finished",
        "description",
    )

    def form_valid(self, form):
        form.save()
        return redirect(reverse("customers:shop-lease-customer-list"))


def shoplease_customer_search(request):

    deposit = int(request.GET.get("deposit", 0))
    month_fee = int(request.GET.get("month_fee", 0))
    area_m2 = int(request.GET.get("area_m2", 0))
    parking = request.GET.get("parking")
    elevator = request.GET.get("elevator")
    not_finished = request.GET.get("not_finished")
    finished = request.GET.get("finished")
   
    filter_args = {}
    filter_args["deposit__lte"] = deposit
    filter_args["month_fee__lte"] = month_fee
    filter_args["area_m2__gte"] = area_m2
    if parking == "on":
        filter_args["parking"] = True
    if elevator == "on":
        filter_args["elevator"] = True
    if not_finished == "on":
        filter_args["not_finished"] = True
    if finished == "on":
        filter_args["finished"] = True
    shoplease_customers = models.ShopLeaseCustomer.objects.filter(**filter_args)
    return render(request, "customers/shoplease/shoplease_search.html", {**filter_args, "shoplease_customers": shoplease_customers})


def shoplease_customer_delete(request, pk):
    shoplease_customer = models.ShopLeaseCustomer.objects.filter(pk=pk).delete()
    return redirect(reverse("customers:shop-lease-customer-list"))


"""below housedealing"""

class HouseDealingCustomerList(ListView):
    model = models.HouseDealingCustomer
    context_object_name = 'housedealing_customers'
    template_name = 'customers/housedealing/housedealing_list.html'


class HouseDealingCustomerDeatil(DetailView):
    model = models.HouseDealingCustomer
    template_name = 'customers/housedealing/housedealing_detail.html'


class HouseDealingCustomerCreating(CreateView):
    form_class = forms.HouseDealingCustomerForm
    template_name = 'customers/housedealing/housedealing_creating.html'

    def form_valid(self, form):
        form.save()
        return redirect(reverse("customers:house-dealing-customer-list"))


class HouseDealingCustomerUpdate(UpdateView):
    model = models.HouseDealingCustomer
    template_name = "customers/housedealing/housedealing_update.html"
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

    def form_valid(self, form):
        form.save()
        return redirect(reverse("customers:house-dealing-customer-list"))


def housedealing_customer_search(request):

    deposit = int(request.GET.get("deposit", 0))
    price = int(request.GET.get("price", 0))
    room = request.GET.get("room", 0)
    area_m2 = int(request.GET.get("area_m2", 0))
    parking = request.GET.get("parking")
    elevator = request.GET.get("elevator")
    not_finished = request.GET.get("not_finished")
    finished = request.GET.get("finished")
   
    filter_args = {}
    filter_args["price__lte"] = price
    filter_args["area_m2__gte"] = area_m2
    filter_args["room__contains"] = room
    if parking == "on":
        filter_args["parking"] = True
    if elevator == "on":
        filter_args["elevator"] = True
    if not_finished == "on":
        filter_args["not_finished"] = True
    if finished == "on":
        filter_args["finished"] = True
    housedealing_customers = models.HouseDealingCustomer.objects.filter(**filter_args)
    return render(request, "customers/housedealing/housedealing_search.html", {**filter_args, "housedealing_customers": housedealing_customers})


def housedealing_customer_delete(request, pk):
    housedealing_customer = models.HouseDealingCustomer.objects.filter(pk=pk).delete()
    return redirect(reverse("customers:house-dealing-customer-list"))


"""below buildingdealing"""

class BuildingDealingCustomerList(ListView):
    model = models.BuildingDealingCustomer
    context_object_name = 'buildingdealing_customers'
    template_name = 'customers/buildingdealing/buildingdealing_list.html'


class BuildingDealingCustomerDeatil(DetailView):
    model = models.BuildingDealingCustomer
    template_name = 'customers/buildingdealing/buildingdealing_detail.html'


class BuildingDealingCustomerCreating(CreateView):
    form_class = forms.BuildingDealingCustomerForm
    template_name = 'customers/buildingdealing/buildingdealing_creating.html'

    def form_valid(self, form):
        form.save()
        return redirect(reverse("customers:building-dealing-customer-list"))


class BuildingDealingCustomerUpdate(UpdateView):
    model = models.BuildingDealingCustomer
    template_name = "customers/buildingdealing/buildingdealing_update.html"
    fields = (
        "guest_phone",
        "price",
        "elevator",
        "description",
        "not_finished",
        "finished",
    )

    def form_valid(self, form):
        form.save()
        return redirect(reverse("customers:building-dealing-customer-list"))


def buildingdealing_customer_search(request):

    price = int(request.GET.get("price", 0))
    elevator = request.GET.get("elevator")
    not_finished = request.GET.get("not_finished")
    finished = request.GET.get("finished")
   
    filter_args = {}
    filter_args["price__lte"] = price
    if elevator == "on":
        filter_args["elevator"] = True
    if not_finished == "on":
        filter_args["not_finished"] = True
    if finished == "on":
        filter_args["finished"] = True
    buildingdealing_customers = models.BuildingDealingCustomer.objects.filter(**filter_args)
    return render(request, "customers/buildingdealing/buildingdealing_search.html", {**filter_args, "buildingdealing_customers": buildingdealing_customers})


def buildingdealing_customer_delete(request, pk):
    buildingdealing_customer = models.BuildingDealingCustomer.objects.filter(pk=pk).delete()
    return redirect(reverse("customers:building-dealing-customer-list"))