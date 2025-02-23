# CookieShop

An online bakery shop built with Django, featuring Ajax-powered cart, user authentication, admin dashboard, and
PostgreSQL.

## Features

- **Ajax-Powered Cart**: Add and remove products from the cart without page reload.
- **User Authentication**: Secure registration, login, and password recovery.
- **Admin Dashboard**: Manage products, orders, and users efficiently.
- **PostgreSQL Database**: Robust and scalable data storage.

## Project Overview

CookieShop is designed to showcase advanced backend development skills using Django. It is suitable for small to
medium-sized bakery businesses aiming to provide an online shopping experience for their customers.

---

## Screenshots

Here are some snapshots of the project to give you a better idea of its features and design:

### Home Page

![Home Page](/static/img/github_images/home.png "Home Page")
> A clean and welcoming homepage for users to browse products.

### Admin Dashboard

![Admin Dashboard](/static/img/github_images/Admin.png "Admin Dashboard")
> Powerful tools for managing the shop, including products, orders, and users.

### Shopping Cart

![Shopping Cart](/static/img/github_images/cart.png "Shopping Cart")
> An Ajax-powered cart for a seamless shopping experience.

### Swagger Page
![Shopping Cart](/static/img/github_images/swagger.png "Shopping Cart")
> An interactive API documentation that allows developers to explore and test the API endpoints.

---

## How to Run

### Prerequisites

To run this project, ensure you have the following installed:

- **Python**: Version 3.8 or higher
- **Django**: Version 3.2 or higher
- **PostgreSQL**: A running instance for database management

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AliNamavar/CookieShop.git
   cd CookieShop
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**
   Update the `DATABASES` setting in `settings.py` to match your PostgreSQL configuration:
   ```python
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project_db',  
        'USER': 'postgres',  
        'PASSWORD': '123',  
        'HOST': 'localhost',  
        'PORT': '5432',  
    
   }
   }
   ```

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000` to view the application.

---

## Folder Structure

```
CookieShop/
├── account_module/       # User authentication and profile management
├── article_module/       # Blog and article functionality
├── contact_us_module/    # Contact form and inquiries
├── cookie_project/       # Main project settings and URLs
├── favorite_module/      # Wishlist management
├── home_module/          # Landing page and homepage logic
├── order_module/         # Order and cart management
├── product_module/       # Product catalog and details
├── site_module/          # Site-wide configurations
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
├── uploads/              # Uploaded media files
├── utils/                # Utility functions and helpers
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

If you have any questions or issues, feel free to open an [issue](https://github.com/AliNamavar/CookieShop/issues) or
contact me directly via GitHub.

---

## Why Choose CookieShop?

This project demonstrates expertise in backend development with Django, showcasing skills in:

## Why Choose CookieShop?

CookieShop is a comprehensive project showcasing advanced skills in backend development using Django. Key highlights
include:

- **Modular Design**: Implementation of modules for managing products, orders, articles, users, and shopping carts.
- **User Authentication**: Secure user registration, login, password recovery, and email verification system.
- **Commenting System**: Users can leave comments on articles, with admin tools for moderation.
- **Class-Based Views (CBVs)**: Utilized for cleaner and more efficient code structure.
- **Database Design**: Built with Django ORM and PostgreSQL for scalable and efficient data management.
- **Ajax-Powered Features**: Seamless shopping cart updates without page reloads.
- **Custom Admin Panel**: Enhanced tools for administrators to manage content and users.
- **Payment Gateway Integration**: Secure payment system for fast and easy checkout.
- **Version Control**: Git and GitHub used for source control and collaboration.

---
