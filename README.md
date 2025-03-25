# Task Management API

## Overview
This is a Task Management API built using Django and Django REST Framework. The API allows users to:
- Create tasks
- Assign tasks to users
- Retrieve tasks assigned to specific users

## Requirements
- Python 3.12.3
- Django 5.1.7
- Django REST Framework 3.15.2

## Installation

### 1. Clone the Repository
```sh
$ git clone https://github.com/GovindHanswal/task-manager-django.git
$ cd task-manager-django
```

### 2. Create a Virtual Environment
```sh
$ python3 -m venv .venv
$ source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### 5. Create a Superuser
```sh
$ python manage.py createsuperuser
```

### 6. Run the Server
```sh
$ python manage.py runserver
```

## API Endpoints

### 1. Create a Task
**Endpoint:** `POST /api/tasks/`

**Request Body:**
```json
{
  "name": "Develop Feature X",
  "description": "Create a new feature in the application",
  "task_type": "development",
  "status": "pending"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Develop Feature X",
  "description": "Create a new feature in the application",
  "task_type": "development",
  "created_at": "2025-03-26T10:00:00Z",
  "completed_at": null,
  "status": "pending",
  "assigned_users": []
}
```

### 2. Assign a Task to Users
**Endpoint:** `POST /api/tasks/{task_id}/assign/`

**Request Body:**
```json
{
  "assigned_users": [1, 2]
}
```

**Response:**
```json
{
  "message": "Task assigned successfully"
}
```

### 3. Retrieve Tasks Assigned to a User
**Endpoint:** `GET /api/users/{user_id}/tasks/`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Develop Feature X",
    "description": "Create a new feature in the application",
    "task_type": "development",
    "created_at": "2025-03-26T10:00:00Z",
    "completed_at": null,
    "status": "pending",
    "assigned_users": [
      {
        "id": 1,
        "username": "johndoe",
        "email": "johndoe@example.com",
        "mobile": "9876543210",
        "department": "backend"
      }
    ]
  }
]
```

## Edge Cases Handled
- **Validation Errors:** If required fields are missing or have invalid data, the API returns `400 Bad Request` with details.
- **Nonexistent Users or Tasks:** If the requested user or task does not exist, the API returns `404 Not Found`.
- **Duplicate Assignments:** Users assigned to a task multiple times are prevented from duplication.

## License
This project is licensed under the MIT License.

## Author
- **Govind Hanswal** - [GitHub](https://github.com/GovindHanswal)


