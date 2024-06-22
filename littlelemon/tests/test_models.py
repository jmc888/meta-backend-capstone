import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from restaurant.models import Booking, MenuItem


class BookingModelTest(TestCase):
    def test_create_booking(self):
        # Test creating a new booking with valid information
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guest=4,
            reservation_date=datetime.date.today(),
            reservation_slot=12,
        )
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guest, 4)

    def test_booking_unique_together_constraint(self):
        # Test the unique together constraint
        date = datetime.date.today()
        Booking.objects.create(
            name="Jane Doe", no_of_guest=3, reservation_date=date, reservation_slot=13
        )
        with self.assertRaises(IntegrityError):
            Booking.objects.create(
                name="John Doe",
                no_of_guest=2,
                reservation_date=date,
                reservation_slot=13,
            )

    def test_booking_no_of_guest_validator(self):
        # Test validator for number of guests
        with self.assertRaises(ValidationError):
            Booking(
                name="Invalid Guests",
                no_of_guest=7,  # Invalid as per validator settings
                reservation_date=datetime.date.today(),
                reservation_slot=15,
            ).full_clean()


class MenuItemModelTest(TestCase):
    def test_create_menu_item(self):
        # Test creating a menu item with valid information
        item = MenuItem.objects.create(
            title="Burger",
            price=9.99,
            inventory=3,
            item_description="Delicious beef burger",
        )
        self.assertEqual(item.title, "Burger")
        self.assertEqual(item.price, 9.99)
        self.assertEqual(item.get_item(), "Burger : 9.99")

    def test_menu_item_unique_title(self):
        # Test uniqueness of the menu item title
        MenuItem.objects.create(title="Unique Salad", price=5.99, inventory=2)
        with self.assertRaises(IntegrityError):
            MenuItem.objects.create(title="Unique Salad", price=6.99, inventory=1)

    def test_menu_item_inventory_validator(self):
        # Test inventory validator
        with self.assertRaises(ValidationError):
            MenuItem(
                title="Sandwich",
                price=4.99,
                inventory=0,  # Invalid as per validator settings
            ).full_clean()
