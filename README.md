# django-url-shortener
URL-Shortener: A project built with django fot shortening urls

## Overview

This is a URL shortener web application built using Django, HTML, CSS, and Bootstrap. It allows users to shorten long URLs into more manageable and shareable links. The application provides a simple and user-friendly interface to input a URL and obtain a shortened version.

## Features

- Shorten long URLs to a more concise format.
- Easily copy and share shortened URLs.
- Visually appealing user interface using Bootstrap and CSS.
- Detailed analytics on shortened URLs, including click counts and referrers (optional).

## Getting Started

To get started with this project, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/SyreCollins/django-url-shortener.git
Setup Virtual Environment:

bash
Copy code
cd django-url-shortener
python -m venv venv
source venv/bin/activate (Linux/macOS)
venv\Scripts\activate (Windows)
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Start the Development Server:

bash
Copy code
python manage.py runserver
Access the Application:

Open your web browser and go to http://localhost:8000 to access the URL shortener.

** Usage **
Visit the URL shortener web application.
Enter a long URL in the provided input field.
Click the "Shorten URL" button.
You will receive a shortened URL.
Copy and share the shortened URL.
Customization
You can customize the project further by:

** Adding analytics and tracking functionality. **
Enhancing the user interface and design.
Adding user authentication to track and manage shortened URLs.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

** Fork the repository. **
Create a new branch for your feature or bug fix.
Make your changes.
Test your changes to ensure they work as expected.
Submit a pull request to the main branch of the original repository.

** License **
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
Author: Michael Collins
Email: therealcollins45@gmail.com
GitHub: SyreCollins
