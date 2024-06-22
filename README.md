# meta-backend-capstone
Repository for capstone project of Coursera back-end developer course 

## Installation
Set up Python virtual environment.
```bash
pipenv install
pipenv shell
cd littlelemon
```
Set up your own database and update the corresponding datebase settings.
Create Django models in database and run Django development server.

```bash
python manage.py migrate
python manage.py runserver
```
Access the web application at http://localhost:8000/restaurant/.

## API Documentation

### Base URL
All URLs referenced in this documentation have the base part as follows:
```bash
http://127.0.0.1:8000/api/
```
### Register API User

**POST /api/registration/**

Request:
```json
{
    "username": "yourusername",
    "email": "youremail",
    "password": "yourpassword"
}
```
Response
```json
// 201 Created
{
    "username": "yourusername",
    "email": "youremail"
}
```

### Authentication

**POST /api/auth/token/login/**

Request:
```json
{
    "username": "yourusername",
    "password": "yourpassword"
}
```
Response
```json
// 200 OK
{
    "auth_token": "yourtoken"
}
```
### Endpoints (Token authentication required)

#### Get all bookings
**GET /api/bookings/**

Response:
```json
// 200 OK
[
	{
		"id": 1,
		"name": "name1",
		"no_of_guest": 3,
		"reservation_date": "2024-06-22",
		"reservation_slot": 11
	},
	{
		"id": 2,
		"name": "name2",
		"no_of_guest": 2,
		"reservation_date": "2024-06-23",
		"reservation_slot": 18
	}
]
```
**POST**, **PUT**, **PATCH**, and **DELETE** method are reserved for admin users only.

#### Get single booking by ID
**GET /api/bookings/{bookingId}**

Response:
```json
// 200 OK
{
    "id": 1,
    "name": "name1",
    "no_of_guest": 3,
    "reservation_date": "2024-06-22",
    "reservation_slot": 11
}
```
**POST**, **PUT**, **PATCH**, and **DELETE** method are reserved for admin users only.


#### Get all menu items
**GET /api/menu-items/**

Response:
```json
// 200 OK
[
	{
		"id": 1,
		"title": "Greek salad",
		"price": "12.00",
		"inventory": 1,
		"item_description": "Our famous Greek salad of crispy lettuce, peppers, olives, and our Chicago-style feta cheese. Garnished with crispy onion and salty capers."
	},
	{
		"id": 2,
		"title": "Grilled fish",
		"price": "9.00",
		"inventory": 1,
		"item_description": "The fish is swiftly grilled over medium- or high-heat coals or over medium- or high-heat gas grill burners. Thinner fillets and steaks are grilled over direct fire."
	},
	{
		"id": 3,
		"title": "Bruschetta",
		"price": "11.00",
		"inventory": 1,
		"item_description": "An Italian antipasto called bruschetta is made of grilled bread that has been smeared with garlic and seasoned with salt and olive oil. Toppings of tomato, veggies, beans, cured pork, or cheese are examples of variations. In Italy, a brustolina grill is frequently used to create bruschetta."
	},
	{
		"id": 4,
		"title": "Lemon dessert",
		"price": "7.00",
		"inventory": 1,
		"item_description": "This cake is adored not only for its flavor but also for its texture and simplicity. A base of creamed butter and sugar, eggs, lemon, milk, and flour are among the most basic ingredients. We omitted the brown sugar and substituted extra granulated sugar instead."
	}
]
```
**POST**, **PUT**, **PATCH**, and **DELETE** method are reserved for admin users only.

#### Get single menu item by ID
**GET /api/menu-items/1**

Response:
```json
// 200 OK
{
	"id": 1,
	"title": "Greek salad",
	"price": "12.00",
	"inventory": 1,
	"item_description": "Our famous Greek salad of crispy lettuce, peppers, olives, and our Chicago-style feta cheese. Garnished with crispy onion and salty capers."
}
```
**POST**, **PUT**, **PATCH**, and **DELETE** method are reserved for admin users only.
