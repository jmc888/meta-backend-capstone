from django.shortcuts import render
from .serializers import BookingSerializer, MenuItemSerializer
from .models import Booking, MenuItem
from rest_framework import viewsets, permissions
from rest_framework import generics


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
