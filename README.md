# Mini Blog 📝

A minimal yet powerful blog application built with Django. This project is ideal for learning, personal blogging, or as a foundation for a larger content management system (CMS).

## Features

- User registration and login
- Post creation, editing, and deletion
- Comment system
- Post detail view
- Clean and responsive UI

## Tech Stack

- **Backend:** Django
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS, Tailwind CSS
- **Authentication:** Django's built-in auth system

## Project Structure

```
mini-blog/
├── blogapp/            # Core blog app
    ├──  Templates      # HTML templates
├── config/             # Project settings and URLs
├── media/              # media files
├── static/             # Static files (CSS, JS)
├── manage.py
└── requirements.txt
```

## Getting Started

Follow these steps to set up the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/adubiblessed/mini-blog.git
cd mini-blog
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Admin Access

To access the admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Then log in at: `http://127.0.0.1:8000/admin/`

## Running Tests

```bash
python manage.py test
```

## Contributing

Contributions are welcome! Fork the repo and open a pull request with your changes.


---

> Built with ❤️ by [@adubiblessed](https://github.com/adubiblessed)
