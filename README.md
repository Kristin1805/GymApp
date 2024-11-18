# Gym Management App

## Overview

The Gym Management App is a Django-based web application designed to streamline gym operations by enabling member enrollment, managing trainers, organizing workout plans, and handling payments. This project facilitates both gym members and staff by providing an intuitive interface for registering, updating profiles, viewing workout plans, and managing memberships. The application incorporates user authentication, role-based permissions, and a structured workflow for gym management.

## Features

- **User Authentication**: Secure registration, login, and logout functionalities with profile-based permissions for trainers and regular members.
- **Profile Management**: Members and trainers can update their profiles, including contact details, address, and membership information.
- **Workout Plans**: Trainers can create, edit, and delete workout plans, allowing customization for different subscription types (e.g., Gym, Cross Fit, Personal Training).
- **Enrollment & Payment Processing**: Users can enroll in various plans and make payments (simulated payment processing included).
- **Trainer Management**: Administrators can manage trainers, including setting permissions and updating salary information.
- **Role-Based Access Control**: Role-based permissions for accessing specific pages and actions, enhancing security and usability.

## Technologies

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL, managed through Django ORM
- **Dependencies**: Django, Django Forms, Django Auth, Django Signals

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd GymManagementApp
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   - Ensure you have PostgreSQL installed and running.
   - Create a database named `gymapp`.
   - Update the `DATABASES` section in `settings.py` if necessary:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'gymapp',
             'USER': '...',
             'PASSWORD': '...',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for accessing the admin panel)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000`

## Usage

1. **Sign Up**: Register a new user through the signup form.
2. **Login**: Use your credentials to log in to access member or trainer features.
3. **Profile Management**: Update your profile with additional details such as address, contact information, and other optional fields.
4. **Browse Workout Plans**: Enroll in a workout plan suited to your preferences.
5. **Payment Processing**: Use the payment form to simulate payment processing and activate your plan.
6. **Admin Panel**: The superuser can manage profiles, trainers, and workout plans in the Django admin interface at `/admin`.

## File Structure

- **GymApp/** - Main Django application directory.
  - **enrolls/** - Manages user enrollment and payment functionality.
  - **profiles/** - Handles user profiles and profile editing.
  - **trainers/** - Manages trainer details, permissions, and salary information.
  - **workouts/** - Handles workout plans and related functionalities.
  - **templates/** - HTML templates for the application's frontend views.
  - **static/** - CSS, JavaScript, and image files.
  - **media/** - Uploaded files, including profile images and workout images.

## Contributing

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature-branch-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push the branch**:
   ```bash
   git push origin feature-branch-name
   ```
5. **Create a Pull Request**

