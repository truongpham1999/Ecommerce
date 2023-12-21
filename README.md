# Ecommerce
E-commerce website using Django

## Overview
Welcome to our Django-based E-commerce platform. Our goal is to deliver an intuitive and comprehensive online shopping experience. This robust application features a sophisticated cart system, user authentication, profile management, and responsive design, ensuring access across various devices.

## Distinctiveness & Complexity:
- This project is different from other CS50W projects. This project is more complex than Project 2 and Project 4, because this application handles the Cart session, where users can add products into the cart, and those products will be added to the user's cart if they log in to their account.
- What sets this application apart is the depth of its features and the complexity behind them. Unlike simpler projects, this E-commerce site simulates a real-world shopping experience. It supports anonymous cart handling, where potential purchases are stored before user authentication, and integrates these items upon login. The application also handles complex user interactions such as account verification via email, detailed order tracking, and user profile management.

## Features
- **User Authentication**: Secure registration and login process with email verification.
- **Cart System**: Dynamic cart sessions allow for adding and modifying product selections.
- **Order Management**: After purchase, users can track their orders through their account.
- **Profile Management**: Users can update personal information and manage their shipping details.
- **Responsive Design**: The interface adapts to screen size for optimal viewing on all devices.

1. Register
2. Log in
3. View products 
4. User management (delete account, update profile...)
5. Email verification (sending a verification link to email)
6. Shipping and Order Management
7. Reset password
8. Shopping cart sessions
9. Paginator
10. Responsive design for mobile and desktop

## Technologies Used
- Python
- Django
- JavaScript (AJAX, DOM loading)
- HTML
- CSS
- Bootstrap
- SQLite
- Django ORM

- **Backend**: Python with Django, harnessing Django's robust ORM for database interactions.
- **Frontend**: HTML, CSS with Bootstrap for styling, and JavaScript for dynamic content loading.
- **Database**: SQLite for lightweight data management.
- **Additional Tools**: AJAX for asynchronous web requests, enhancing user experience without full page reloads.

## Project Structure
The application is organized into distinct Django apps, each responsible for a set of related features:

- `ecommerce/`: The main project directory housing settings and root configurations.
- `account/`: Handles user accounts, registration, and profile management.
- `cart/`: Manages the shopping cart logic, including session handling and product management.
- `payment/`: Processes payments and order management.
- `store/`: Displays products and handles the core e-commerce functionality.
- `static/`: Contains CSS, JavaScript, and media assets for the frontend.

## Getting Started
To run this application locally:
1. **Clone the Repository**: Obtain a copy of the code on your machine.
2. **Set Up Environment**: Navigate to the project directory and install dependencies with `pip install -r requirements.txt`.
3. **Launch the Server**: Execute `python manage.py runserver` to start the development server.

