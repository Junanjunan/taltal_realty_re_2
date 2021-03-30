from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from . import models, forms
from books import models as models_users


class RoomLeaseList(ListView):
    model = models.RoomLease
    context_object_name = 'roomlease'
    template_name = 'books/roomlease/roomlease_list.html'


class RoomLeaseDeatil(DetailView):
    model = models.RoomLease
    template_name = 'books/roomlease/roomlease_detail.html'


class RoomLeaseCreating(CreateView):
    form_class = forms.RoomLeaseForm
    template_name = 'books/roomlease/roomlease_creating.html'

    def form_valid(self, form):
        book = form.save()
        book.realtor = self.request.user                    
        book.save()
        return redirect(reverse("books:room-lease-list"))

    # def get_success_url(self):
    #     return reverse("books:room-lease-list")   # 위 아래 둘 다 가능


class RoomLeaseUpdate(UpdateView):
    model = models.RoomLease
    template_name = "books/roomlease/roomlease_update.html"
    fields = ('address',
              "deposit",
              "month_fee",
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
              "description")

    def form_valid(self, form):
        form.save()
        return redirect(reverse("books:room-lease-list"))


def roomlease_search(request):

    address = request.GET.get("address")
    deposit = int(request.GET.get("deposit", 0))
    month_fee = int(request.GET.get("month_fee", 0))
    area_m2 = int(request.GET.get("area_m2", 0))
    room = request.GET.get("room", 0)
    parking = request.GET.get("parking")
    elevator = request.GET.get("elevator")
    loan = request.GET.get("loan")
    empty = request.GET.get("empty")
    naver = request.GET.get("naver")
    not_finished = request.GET.get("not_finished")
    finished = request.GET.get("finished")
    description = request.GET.get("description")

    filter_args = {}
    filter_args["address__contains"] = address
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
    if empty == "on":
        filter_args["empty"] = True
    if naver == "on":
        filter_args["naver"] = True
    if not_finished == "on":
        filter_args["not_finished"] = True
    if finished == "on":
        filter_args["finished"] = True
    lease = models.RoomLease.objects.filter(**filter_args)
    return render(request, "books/roomlease/roomlease_search.html", {**filter_args, "lease": lease})


def roomlease_delete(request, pk):
    room = models.RoomLease.objects.filter(pk=pk).delete()
    return redirect(reverse("books:room-lease-list"))


"""below house dealing"""


class RoomDealingList(ListView):
    model = models.RoomDealing
    context_object_name = 'roomdealing'
    template_name = 'books/roomdealing/roomdealing_list.html'


class RoomDealingDeatil(DetailView):
    model = models.RoomDealing
    template_name = 'books/roomdealing/roomdealing_detail.html'


class RoomDealingCreating(CreateView):
    form_class = forms.RoomDealingForm
    template_name = 'books/roomdealing/roomdealing_creating.html'

    def form_valid(self, form):
        form.save()
        return redirect(reverse("books:room-dealing-list"))


class RoomDealingUpdate(UpdateView):
    model = models.RoomDealing
    template_name = "books/roomdealing/roomdealing_update.html"
    fields = ('address',
              'price',
              "deposit",
              "month_fee",
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
              "description")

    def form_valid(self, form):
        form.save()
        return redirect(reverse("books:room-dealing-list"))


def roomdealing_search(request):

    address = request.GET.get("address")
    price = int(request.GET.get("price", 0))
    deposit = int(request.GET.get("deposit", 0))
    month_fee = int(request.GET.get("month_fee", 0))
    area_m2 = int(request.GET.get("area_m2", 0))
    room = request.GET.get("room", 0)
    parking = request.GET.get("parking")
    elevator = request.GET.get("elevator")
    loan = request.GET.get("loan")
    empty = request.GET.get("empty")
    naver = request.GET.get("naver")
    not_finished = request.GET.get("not_finished")
    finished = request.GET.get("finished")
    description = request.GET.get("description")

    filter_args = {}
    filter_args["address__contains"] = address
    filter_args["price__lte"] = price
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
    if empty == "on":
        filter_args["empty"] = True
    if naver == "on":
        filter_args["naver"] = True
    if not_finished == "on":
        filter_args["not_finished"] = True
    if finished == "on":
        filter_args["finished"] = True
    lease = models.RoomDealing.objects.filter(**filter_args)
    return render(request, "books/roomdealing/roomdealing_search.html", {**filter_args, "lease": lease})


def roomdealing_delete(request, pk):
    room = models.RoomDealing.objects.filter(pk=pk).delete()
    return redirect(reverse("books:room-dealing-list"))


"""below store"""


class StoreLeaseList(ListView):
    model = models.StoreLease
    context_object_name = 'storelease'
    template_name = 'books/storelease/storelease_list.html'


class StoreLeaseDeatil(DetailView):
    model = models.StoreLease
    template_name = 'books/storelease/storelease_detail.html'


class StoreLeaseCreating(CreateView):
    form_class = forms.StoreLeaseForm
    template_name = 'books/storelease/storelease_creating.html'

    def form_valid(self, form):
        form.save()
        return redirect(reverse("books:store-lease-list"))

    # def get_success_url(self):
    #     return reverse("books:room-lease-list")   # 위 아래 둘 다 가능


class StoreLeaseUpdate(UpdateView):
    model = models.RoomLease
    template_name = "books/storelease/storelease_update.html"
    fields = ('address',
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
              "description")

    def form_valid(self, form):
        form.save()
        return redirect(reverse("books:store-lease-list"))


def storelease_search(request):

    address = request.GET.get("address")
    right_deposit = int(request.GET.get("right_deposit", 0))
    deposit = int(request.GET.get("deposit", 0))
    month_fee = int(request.GET.get("month_fee", 0))
    area_m2 = int(request.GET.get("area_m2", 0))
    parking = request.GET.get("parking")
    elevator = request.GET.get("elevator")
    empty = request.GET.get("empty")
    naver = request.GET.get("naver")
    not_finished = request.GET.get("not_finished")
    finished = request.GET.get("finished")
    description = request.GET.get("description")

    filter_args = {}
    filter_args["address__contains"] = address
    filter_args["right_deposit__lte"] = right_deposit
    filter_args["deposit__lte"] = deposit
    filter_args["month_fee__lte"] = month_fee
    filter_args["area_m2__gte"] = area_m2
    if parking == "on":
        filter_args["parking"] = True
    if elevator == "on":
        filter_args["elevator"] = True
    if empty == "on":
        filter_args["empty"] = True
    if naver == "on":
        filter_args["naver"] = True
    if not_finished == "on":
        filter_args["not_finished"] = True
    if finished == "on":
        filter_args["finished"] = True
    lease = models.StoreLease.objects.filter(**filter_args)
    return render(request, "books/storelease/storelease_search.html", {**filter_args, "lease": lease})


def storelease_delete(request, pk):
    room = models.StoreLease.objects.filter(pk=pk).delete()
    return redirect(reverse("books:store-lease-list"))


"""below building"""


class BuildingDealingList(ListView):
    model = models.BuildingDealing
    context_object_name = 'buildingdealing'
    template_name = 'books/buildingdealing/buildingdealing_list.html'


class BuildingDealingDeatil(DetailView):
    model = models.BuildingDealing
    template_name = 'books/buildingdealing/buildingdealing_detail.html'


class BuildingDealingCreating(CreateView):
    form_class = forms.BuildingDealingForm
    template_name = 'books/buildingdealing/buildingdealing_creating.html'

    def form_valid(self, form):
        form.save()
        return redirect(reverse("books:building-dealing-list"))


class BuildingDealingUpdate(UpdateView):
    model = models.BuildingDealing
    template_name = "books/buildingdealing/buildingdealing_update.html"
    fields = ('address',
              'price',
              'equity',
              "deposit",
              "month_fee",
              "land_m2",
              'land_type',
              "owner_phone",
              "elevator",
              "empty",
              "naver",
              "not_finished",
              "finished",
              "description")

    def form_valid(self, form):
        form.save()
        return redirect(reverse("books:building-dealing-list"))


def buildingdealing_search(request):

    address = request.GET.get("address")
    price = int(request.GET.get("price", 0))
    land_m2 = int(request.GET.get("area_m2", 0))
    elevator = request.GET.get("elevator")
    empty = request.GET.get("empty")
    naver = request.GET.get("naver")
    not_finished = request.GET.get("not_finished")
    finished = request.GET.get("finished")

    filter_args = {}
    filter_args["address__contains"] = address
    filter_args["price__lte"] = price
    filter_args["land_m2__gte"] = land_m2
    if elevator == "on":
        filter_args["elevator"] = True
    if empty == "on":
        filter_args["empty"] = True
    if naver == "on":
        filter_args["naver"] = True
    if not_finished == "on":
        filter_args["not_finished"] = True
    if finished == "on":
        filter_args["finished"] = True
    buildingdealing = models.BuildingDealing.objects.filter(**filter_args)
    return render(request, "books/buildingdealing/buildingdealing_search.html", {**filter_args, "buildingdealing": buildingdealing})


def buildingdealing_delete(request, pk):
    building = models.BuildingDealing.objects.filter(pk=pk).delete()
    return redirect(reverse("books:building-dealing-list"))
