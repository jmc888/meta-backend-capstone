from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6),
        ]
    )
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(
        validators=[
            MinValueValidator(11),
            MaxValueValidator(19),
        ]
    )

    class Meta:
        unique_together = ("reservation_date", "reservation_slot")

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )

    item_description = models.TextField(max_length=1000, default="")

    def get_item(self):
        return f"{self.title} : {str(self.price)}"

    def __str__(self):
        return self.title
