# TODO Web Django REST APIs

## Project Overview
This is a Django REST Framework (DRF) backend API for a Todo Web Application. The API provides full CRUD (Create, Read, Update, Delete) operations for managing todo items and supports frontend interactions.

## Frontend Repository
Frontend React Application: [To-Do-Web-App](https://github.com/ManiSetharasipalli/To-Do-Web-App.git)

## Deployment
Deployed on PythonAnywhere: [https://tododjangoapis.pythonanywhere.com](https://tododjangoapis.pythonanywhere.com)

## Key Features
- RESTful API endpoints for Todo management
- Implemented using Django REST Framework ViewSets
- Supports complete CRUD operations
- Simple and efficient API design

## Technologies Used
- Django
- Django REST Framework
- Python

## Learning Journey
During the development of this project, I learned:
- Building RESTful APIs using Django REST Framework
- Implementing ViewSets for efficient CRUD operations
- API design and best practices

## Getting Started

### Prerequisites
- Python 3.10+
- Django
- Django REST Framework

### Installation
1. Clone the repository
```bash
git clone (https://github.com/ManiSetharasipalli/TODO_Web_Django_APIS.git)
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

## API Endpoints

### Tasks Endpoints
- `GET api/tasks` - Fetch all tasks
- `POST api/tasks` - Create new task
- `PUT api/tasks/:id` - Update task
- `PATCH api/tasks/:id` - Toggle task completion status
- `DELETE api/tasks/:id` - Delete specific task
- `DELETE api/tasks/delete_all` - Delete all tasks

## Reference
Book: "Django for APIs: Build Web APIs with Python and Django"
Author: William S. Vincent
Special thanks to the author for guidance in API development
