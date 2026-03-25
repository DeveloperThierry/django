# Django Social App

A lightweight Django web application featuring user authentication, profile management, and a functional posting system.

## 🚀 Features

*   **User Authentication:** Complete Login, Logout, and Registration flow using Django’s built-in auth system.
*   **Post Management:** Logged-in users can create new posts with support for image/file uploads.
*   **Access Control:** Protected routes using `@login_required` decorators.
*   **Security:** Configured for CSRF protection in cloud development environments.

## 🛠️ Tech Stack

*   **Framework:** Django 5.2+
*   **Language:** Python 3.11
*   **Database:** SQLite (Default) / PostgreSQL ready

## 📦 Installation & Setup

1.  Clone the repository:
    ```bash
    git clone [Repo Url](https://github.com/DeveloperThierry/django.git)
    cd myproject
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install django
    ```
4.  Run Migrations:
    ```bash
    python manage.py migrate
    ```
5.  Start the server:
    ```bash
    python manage.py runserver
    ```

## ⚙️ Configuration Notes

If running in a Cloud Workstation or codespace, ensure your `settings.py` includes the following to avoid CSRF 403 errors:

```python
CSRF_TRUSTED_ORIGINS = ['your_localhost']
```
