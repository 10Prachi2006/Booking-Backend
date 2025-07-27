# Booking-backend
Using Databases, APIs, and Django

----------------------------------------------------------------------------------------------



# 📸ScreenShots
<img width="1349" height="715" alt="Screenshot 2025-07-27 at 13-54-14 Little Lemon" src="https://github.com/user-attachments/assets/c5fbef73-09e8-4543-87fb-0db76de2d852" />
<img width="1323" height="1003" alt="Screenshot 2025-07-27 at 13-52-30 Little Lemon" src="https://github.com/user-attachments/assets/6e01073f-57af-48ae-9b7d-f69212fcf1b4" />





----------------------------------------------------------------------------------------------






# Little Lemon Restaurant Booking System

This project is a web application for the Little Lemon restaurant, allowing customers to easily make and manage table reservations. It's built with Django for the backend, MySQL as the database, and a dynamic frontend using HTML, CSS, and JavaScript, leveraging RESTful API principles for seamless user interaction.




----------------------------------------------------------------------------------------------



✨ Features

* **Online Table Reservations:** Customers can book a table by providing their name, desired date, and preferred time slot.
* **Dynamic Slot Availability:** The system displays existing bookings for a selected date and intelligently disables already reserved time slots in real-time, preventing double-bookings.
* **API-Driven Interaction:** Frontend and backend communicate via AJAX (Asynchronous JavaScript and XML) calls to a RESTful API endpoint, providing a smooth user experience without full page reloads.
* **Database Integration:** All reservation data is persistently stored and managed in a MySQL database.
* **Admin Interface:** Django's built-in admin panel allows restaurant staff to manage bookings directly (though not explicitly detailed in the customer-facing features, it's a standard Django capability).


----------------------------------------------------------------------------------------------




🚀 Technologies Used

**Backend:**
* **Python:** The core programming language.
* **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
    * **Django ORM (Object-Relational Mapper):** For interacting with the database using Python objects instead of raw SQL.
    * **Django Migrations:** For managing database schema changes.
    * **Django Views:** To handle request-response cycles and API endpoints.
* **MySQL:** A powerful open-source relational database management system for data storage.
* **Django REST Framework (DRF) principles:** Although a full DRF setup might not be explicitly used, the project utilizes `serializers.serialize('json', ...)` and `HttpResponse(..., content_type='application/json')` to create a basic API endpoint, following RESTful communication patterns.

**Frontend:**
* **HTML5:** For structuring the web content.
* **CSS3:** For styling and layout.
* **JavaScript (ES6+):** For dynamic behavior, including:
    * **Event Listeners:** To react to user interactions (e.g., date selection, button clicks).
    * **`fetch` API:** For making asynchronous HTTP requests (AJAX) to the backend API.
    * **JSON Handling:** Parsing and stringifying JSON data for client-server communication.
    * **DOM Manipulation:** Dynamically updating the reservation list and time slot dropdown based on API responses.





----------------------------------------------------------------------------------------------





⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/little-lemon-booking.git](https://github.com/YourUsername/little-lemon-booking.git)
    cd little-lemon-booking
    ```
    (Replace `YourUsername` with your GitHub username and `little-lemon-booking` with your repository name)

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt # Assuming you have a requirements.txt file
    # If not, install manually:
    # pip install django mysqlclient # or Django<version> and mysqlclient<version>
    ```

4.  **MySQL Database Setup:**
    * Ensure you have **MySQL Server** installed and running on your machine (default port: `3306`).
    * Using MySQL Workbench or your preferred MySQL client, create a new database (e.g., `littlelemon_db`).
    * Create a dedicated MySQL user (e.g., `django_user`) and grant it full privileges on the `littlelemon_db` database.
        ```sql
        -- Example SQL commands (adjust user and database names)
        CREATE DATABASE littlelemon_db;
        CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'your_password';
        GRANT ALL PRIVILEGES ON littlelemon_db.* TO 'django_user'@'localhost';
        FLUSH PRIVILEGES;
        ```

5.  **Configure Django Settings:**
    * Open `littlelemon/settings.py` (located in your project's main directory).
    * Update the `DATABASES` configuration to match your MySQL setup:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'littlelemon_db',  # Your database name
                'USER': 'django_user',      # Your MySQL user
                'PASSWORD': 'your_password', # Your MySQL user's password
                'HOST': '127.0.0.1',        # Or 'localhost'
                'PORT': '3306',
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                }
            }
        }
        ```
    * Ensure `'restaurant'` is listed in your `INSTALLED_APPS`.

6.  **Run Migrations:**
    Apply the database schema changes:
    ```bash
    python manage.py makemigrations restaurant
    python manage.py migrate
    ```

7.  **Create a Superuser (Optional, for Admin Panel Access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin account.

8.  **Run the Django Development Server:**
    ```bash
    python manage.py runserver
    ```





----------------------------------------------------------------------------------------------






🌐 Usage

1.  Open your web browser and go to `http://127.0.0.1:8000/book/` (or the URL mapped to your booking page).
2.  Enter your name, select a reservation date, and choose an available time slot.
3.  Click "Reserve Now". The page will dynamically update with your booking, and the selected time slot will be marked as unavailable for that date.
4.  Change the reservation date to see bookings specific to that date and updated slot availabilities.
5.  You can also access the Django admin panel at `http://127.0.0.1:8000/admin/` using your superuser credentials to manage bookings directly.






----------------------------------------------------------------------------------------------





🤝 Contributing

Feel free to fork this repository, submit issues, or create pull requests.




----------------------------------------------------------------------------------------------






📄 License

This project is licensed under the MIT License.



----------------------------------------------------------------------------------------------




## Author


Prachi Yadav.
