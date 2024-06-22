import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework import generics
from datetime import datetime
from .models import Booking, MenuItem
from .forms import BookingForm
from .serializers import (
    BookingSerializer,
    MenuItemSerializer,
    UserRegistrationSerializer,
)


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def menu(request):
    menu_data = MenuItem.objects.all()

    return render(request, "menu.html", {"menu": menu_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = MenuItem.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})


def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


# Add code for the bookings() view
@csrf_exempt
def bookings(request):
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        if request.method == "POST":
            data = json.load(request)
            exist = (
                Booking.objects.filter(reservation_date=data["reservation_date"])
                .filter(reservation_slot=data["reservation_slot"])
                .exists()
            )
            if exist == False:
                booking = Booking(
                    name=data["name"],
                    no_of_guest=data["no_of_guest"],
                    reservation_date=data["reservation_date"],
                    reservation_slot=data["reservation_slot"],
                )
                booking.save()
            else:
                return HttpResponse(
                    "{'error': 'The slot you requested is not available'}",
                    content_type="application/json",
                )

        date = request.GET.get("date", datetime.today().date())

        bookings = Booking.objects.all().filter(reservation_date=date)
        booking_json = serializers.serialize("json", bookings)

        return HttpResponse(booking_json, content_type="application/json")
    else:
        return HttpResponseBadRequest("Invalid request")


# API
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
