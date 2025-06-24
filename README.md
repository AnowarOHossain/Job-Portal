# Job Portal Bangladesh

Welcome to **Job Portal Bangladesh**, a web application designed to connect job seekers and employers in Bangladesh. Built using Django, HTML, Tailwind CSS, and JavaScript, this platform allows users to post job listings, apply for jobs, and manage their profiles. The application features a modern, responsive design tailored to the Bangladeshi job market.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- User authentication (login, logout, registration)
- Job posting with details (title, company, location, salary, description, requirements)
- Job application submission with cover letter
- Responsive design using Tailwind CSS
- Search functionality for job listings
- Admin panel for managing jobs and applications

## Prerequisites
- Python 3.8 or higher
- Django 4.2 or higher
- Git (for version control)
- A code editor (e.g., VS Code)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AnowarOHossain/job-portal.git
   cd job-portal
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Open your browser and visit `http://127.0.0.1:8000/` to see the application.

## Usage
- **Register/Login**: Use the "Register" or "Login" links to create an account or sign in.
- **Post a Job**: Logged-in users can navigate to "Post Job" to create a new job listing, including title, company, location, salary, description, and requirements.
- **Apply for Jobs**: View job details and submit applications with a cover letter if logged in.
- **Admin Panel**: Access `/admin/` with superuser credentials to manage jobs and applications.

## Project Structure
```
job-portal/
├── job_portal/          # Django project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── jobs/               # Django app for job functionality
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── job_detail.html
│   ├── job_create.html
│   ├── login.html
│   └── register.html
├── static/             # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── manage.py
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

## Contributing
Contributions are welcome! If you'd like to contribute to Job Portal Bangladesh, please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit: `git commit -m "Description of changes"`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request on GitHub.

Please ensure your code follows Django best practices and is tested before submitting.

## License
This project is currently unlicensed. Feel free to contact the maintainer for details on usage rights.

## Contact
- **Author**: Anowar Hossain
- **GitHub**: [AnowarOHossain](https://github.com/AnowarOHossain)
- **Email**: anowarhossain.dev@gmail.com