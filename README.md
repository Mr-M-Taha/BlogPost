[README.md](https://github.com/user-attachments/files/23767343/README.md)
# BlogHub - A Complete Blogging Platform

BlogHub is a full-featured blogging platform built with Django. It allows users to create, read, update, and delete blog posts, as well as manage their own profiles.

## Features

*   **User Authentication:** Users can register, log in, log out, and manage their profiles.
*   **Blog Post Management:** Create, read, update, and delete blog posts.
*   **Responsive Design:** The project uses Bootstrap for a responsive and mobile-friendly layout.
*   **Admin Panel:** A powerful admin panel to manage all aspects of the blog.
*   **Static File Handling:** Serves static files like CSS and JavaScript.

## Technologies Used

*   Python
*   Django
*   HTML
*   CSS
*   Bootstrap
*   SQLite3

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python 3.8+ installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/bloghub.git
    cd bloghub
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.

## Usage

*   **Home Page:** View the latest blog posts.
*   **Register:** Create a new user account.
*   **Login:** Access your account.
*   **Profile:** View and update your profile information.
*   **Create Post:** Write and publish a new blog post.
*   **Update/Delete Post:** Edit or remove your existing posts.
*   **Admin Panel:** Access the admin interface at `/admin/` to manage users and posts.

## Project Structure

```
my_blog/
├── blog_post/
│   ├── blog/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── users/
│   │   ├── migrations/
│   │   ├── templates/
│   │   └── ...
│   ├── blog_post/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── manage.py
│   └── db.sqlite3
└── venv/
```

*   **`blog/`**: The app for handling blog posts.
*   **`users/`**: The app for user authentication and profiles.
*   **`blog_post/`**: The main project directory.
*   **`static/`**: Contains static files (CSS, JavaScript).
*   **`templates/`**: Contains HTML templates for the apps.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
