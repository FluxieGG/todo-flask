# Todo Flask Application

A simple yet feature-rich TODO application built with Flask, featuring user authentication and task management.

## Project Overview

This is a web-based todo application that allows users to create accounts, authenticate, and manage their personal task lists. It includes user registration, login functionality, and full CRUD operations for tasks.

## Features

- **User Authentication**: Secure user registration and login using Flask-Login
- **Task Management**: Create, read, update, and delete tasks
- **User-Specific Tasks**: Each user can only see and manage their own tasks
- **Password Security**: Passwords are hashed using Werkzeug's security utilities
- **Database Management**: SQLAlchemy ORM with Flask-Migrate for database migrations

## Technology Stack

- **Backend Framework**: Flask 3.1.2
- **Database ORM**: SQLAlchemy 2.0.44
- **Authentication**: Flask-Login 0.6.3
- **Database Migrations**: Flask-Migrate 4.1.0
- **Form Handling**: Flask-WTF 1.2.2 & WTForms 3.2.1
- **Frontend**: Jinja2 templating with HTML/CSS

## Project Structure

```
todo-flask/
├── app.py                 # Flask application initialization
├── config.py              # Configuration settings
├── models.py              # Database models (User, Todo)
├── forms.py               # WTForms form definitions
├── routes.py              # Application routes and logic
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore file
├── static/
│   └── css/
│       └── style.css      # Application styling
└── templates/
    ├── base.html          # Base template with navigation
    ├── index.html         # Homepage
    ├── login.html         # Login page
    ├── register.html      # User registration page
    ├── tasks.html         # Tasks list page
    ├── task.html          # Individual task view
    └── task_form.html     # Form for creating/editing tasks
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd todo-flask
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Create environment variables** (optional):
   Create a `.env` file in the project root for configuration:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   ```

## Running the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Database Models

### User Model

- `id`: Primary key
- `username`: Unique username (string)
- `password_hash`: Hashed password (string)
- `todos`: Relationship to Todo items

### Todo Model

- `id`: Primary key
- `title`: Task title
- `description`: Task description
- `user_id`: Foreign key to User
- `user`: Relationship to User
- Additional fields for task management

## Usage

1. **Register**: Create a new account with a username and password
2. **Login**: Sign in with your credentials
3. **Create Tasks**: Add new todo items from the tasks page
4. **Manage Tasks**: Edit or delete your existing tasks
5. **Logout**: Sign out from the application

## Key Files Description

- **app.py**: Flask app initialization, database setup, and extension configuration
- **config.py**: Configuration for database, secret keys, and app settings
- **models.py**: SQLAlchemy models for User and Todo entities
- **forms.py**: WTForms form classes for user input validation
- **routes.py**: Application routes for all pages and API endpoints

## Dependencies

See `requirements.txt` for the complete list of dependencies.

Key packages:

- Flask (web framework)
- Flask-SQLAlchemy (ORM)
- Flask-Login (user session management)
- Flask-Migrate (database migrations)
- Flask-WTF (form protection)

## Development Notes

- The application uses Flask-Login for session management
- User authentication is required to view and manage tasks
- All database changes should be tracked with Flask-Migrate
- CSS styling is located in `static/css/style.css`

---

**Last Updated**: December 2025
