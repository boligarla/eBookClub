# Django Blog App

eBookclub starter website written in Django.

## Overview

This Django web application creates a blog/bookclub, where users can browse available books and write blogs and manage their accounts.

The main features that have currently been implemented are:

* User registration, profile update
* There are models for books, book copies, genre, language and authors.
* Users can view list and detail information for books and authors.
* Admin users can create and manage models. The admin has been optimised (the basic registration is present in admin.py, but commented out).
* Readers can renew reserved books



## Quick Start

To get this project up and running locally on your computer:
1. Set up the : https://django-environ.readthedocs.io/en/latest/
   We recommend using a Python virtual environment.
1. Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   pip3 install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py test # Run the standard tests. These should all pass.
   python manage.py createsuperuser # Create a superuser
   python manage.py runserver
   ```
1. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
1. Create a few test objects of each type.
1. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.