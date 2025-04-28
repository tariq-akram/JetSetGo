# JetSetGo Travel Itinerary Website

JetSetGo is a travel itinerary website designed to help users plan their trips effectively. Built using Django and MySQL, JetSetGo offers a user-friendly interface and robust functionality to streamline the travel planning process.

## Features

- **User Authentication**: Sign up and log in to access the website's features securely.
- **Travel Planner**: Create detailed itineraries for trips, including destination details, travel dates, participant names, and planned activities.
- **Group Booking Management**: Manage group bookings effortlessly by creating bookings, adding members, and tracking booking history.
- **Recommended Destinations**: Explore recommended travel destinations based on user preferences and interests.
- **Responsive Design**: Access the website seamlessly from any device, including desktops, tablets, and smartphones.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **MySQL**: An open-source relational database management system for storing and retrieving data.
- **HTML/CSS/JavaScript**: Front-end development languages for creating the website's layout, style elements, and interactive features.
- **Bootstrap**: A CSS framework for designing responsive and mobile-first websites.

## How to Clone and Run the Project

1. **Clone the repository**  
   First, clone the repository to your local machine by running the following command in your terminal:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the project directory**  
   Once the repository is cloned, navigate to the project folder:
   ```bash
   cd JetSetGo
   ```

3. **Install dependencies**  
   Make sure you have Python and pip installed. Then, install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   This will install all the Python packages required to run the project, including Django and other dependencies listed in the `requirements.txt` file.

4. **Set up the MySQL Database**  
   Before running the server, make sure to set up MySQL for the project. You will need to configure the database settings in the `settings.py` file under the `DATABASES` section. Create a new database and ensure the connection credentials match those in the settings file.

5. **Run database migrations**  
   Run the following command to set up the database schema:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**  
   To access the admin panel, create a superuser by running:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your superuser account.

7. **Run the development server**  
   After all dependencies are installed and the database is set up, you can start the development server:
   ```bash
   python manage.py runserver
   ```

8. **Access the website**  
   Once the server is running, open your browser and visit the following URL:
   ```
   http://localhost:8000
   ```
   You should now be able to access the JetSetGo website and start planning your trips!

## Contributors

- Mohammed Tariq Akram
- Muskan Kwatra
- Mohit Verma
- Laasya Vasaath

## Acknowledgements

Special thanks to all the contributors.

Feel free to add to this project!