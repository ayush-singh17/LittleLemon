# Little Lemon Restaurant API

This is the backend API for the Little Lemon restaurant application, built using Django and Django REST Framework (DRF). It provides API endpoints for managing the restaurant menu, bookings, and user authentication.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation & Setup](#installation--setup)
3. [Running the Server](#running-the-server)
4. [Running Tests](#running-tests)
5. [Database Configuration](#database-configuration)
6. [API Endpoints to Test](#api-endpoints-to-test)
    - [User Registration & Authentication](#1-user-registration--authentication)
    - [Menu Management](#2-menu-management)
    - [Booking Management](#3-booking-management)

---

## Prerequisites

- **Python**: Version 3.14 (or any compatible 3.x version)
- **Pipenv**: Dependency manager for Python
- **MySQL**: The project is pre-configured to connect to a local MySQL instance

---

## Installation & Setup

1. **Clone the Repository** and navigate to the project root:
   ```bash
   cd LittleLemon
   ```

2. **Install Dependencies** using `pipenv`:
   ```bash
   pipenv install
   ```

3. **Activate the Virtual Environment**:
   ```bash
   pipenv shell
   ```

4. **Navigate to the Django Project root**:
   ```bash
   cd littlelemon
   ```

5. **Apply Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

## Running the Server

Start the Django development server:
```bash
python manage.py runserver
```
The API will be accessible locally at `http://127.0.0.1:8000/`.

---

## Running Tests

The project includes model and view unit tests. To execute them, run:
```bash
python manage.py test
```

---

## Database Configuration

The project database configuration can be found in `littlelemon/settings.py`. By default, it expects a local MySQL instance:
- **Engine**: `django.db.backends.mysql`
- **Database Name**: `littlelemon`
- **User**: `root`
- **Password**: `""` (empty)
- **Host**: `localhost`
- **Port**: `3306`

*Note: Make sure your MySQL server is running and a database named `littlelemon` is created before running migrations or starting the server.*

---

## API Endpoints to Test

Here are the primary paths and HTTP methods available for testing. Note that Booking endpoints require authentication.

### 1. User Registration & Authentication

The project uses **Djoser** and **Django REST Framework Token Authentication**.

#### A. User Registration
* **Endpoint**: `POST /auth/users/`
* **Description**: Registers a new user.
* **Payload**:
  ```json
  {
      "username": "newuser",
      "password": "securepassword123",
      "email": "user@example.com"
  }
  ```

#### B. User Profile
* **Endpoint**: `GET /auth/users/me/`
* **Description**: Retrieve the logged-in user profile.
* **Headers**:
  ```http
  Authorization: Token <your_token>
  ```

#### C. Login (Get Auth Token)
You can obtain a token using either the Djoser endpoint or the standard DRF token endpoint.

* **Djoser Login**: `POST /auth/token/login/`
* **DRF Login**: `POST /restaurant/api-token-auth/`
* **Description**: Exchange username and password for a token.
* **Payload**:
  ```json
  {
      "username": "newuser",
      "password": "securepassword123"
  }
  ```
* **Response**:
  ```json
  {
      "auth_token": "a1b2c3d4e5f6g7h8..."
  }
  ```

#### D. Logout
* **Endpoint**: `POST /auth/token/logout/`
* **Description**: Invalidates the user's active session token.
* **Headers**:
  ```http
  Authorization: Token <your_token>
  ```

---

### 2. Menu Management

Menu endpoints do not require authentication by default in the current codebase settings.

#### A. List Menu Items
* **Endpoint**: `GET /restaurant/menu/` (also mapped to `GET /restaurant/menu/menu/`)
* **Description**: Retrieve a list of all menu items.
* **Response**:
  ```json
  [
      {
          "id": 1,
          "title": "IceCream",
          "price": "80.00",
          "inventory": 100
      }
  ]
  ```

#### B. Create Menu Item
* **Endpoint**: `POST /restaurant/menu/` (also mapped to `POST /restaurant/menu/menu/`)
* **Description**: Add a new item to the menu.
* **Payload**:
  ```json
  {
      "title": "Lemon Tart",
      "price": "7.50",
      "inventory": 45
  }
  ```

#### C. Retrieve, Update, or Delete Menu Item
* **Endpoint**: `GET` / `PUT` / `PATCH` / `DELETE` `/restaurant/menu/<id>/` (also mapped to `/restaurant/menu/menu/<id>/`)
* **Description**: View, update, or remove a specific menu item.
* **Payload (for PUT/PATCH)**:
  ```json
  {
      "title": "Lemon Tart (Updated)",
      "price": "8.00",
      "inventory": 40
  }
  ```

---

### 3. Booking Management

These endpoints require authentication. Ensure you pass the `Authorization` header with a valid token.

#### A. List Bookings
* **Endpoint**: `GET /restaurant/booking/tables/`
* **Headers**:
  ```http
  Authorization: Token <your_token>
  ```
* **Description**: Lists all active bookings.

#### B. Create Booking
* **Endpoint**: `POST /restaurant/booking/tables/`
* **Headers**:
  ```http
  Authorization: Token <your_token>
  ```
* **Payload**:
  ```json
  {
      "name": "Alex Mercer",
      "no_of_guests": 4,
      "booking_date": "2026-06-25"
  }
  ```

#### C. Retrieve, Update, or Delete Booking
* **Endpoint**: `GET` / `PUT` / `PATCH` / `DELETE` `/restaurant/booking/tables/<id>/`
* **Headers**:
  ```http
  Authorization: Token <your_token>
  ```
  * **Payload (for PUT/PATCH)**:
  ```json
  {
      "name": "Alex Mercer",
      "no_of_guests": 5,
      "booking_date": "2026-06-26"
  }
  ```
