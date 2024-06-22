from rest_framework import serializers
from .models import Booking, MenuItem
from django.contrib.auth.models import User


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"], email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
