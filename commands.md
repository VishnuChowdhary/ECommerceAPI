# Packages

pip install django
pip install djangorestframework
pip install python-dotenv --To store the passwords and usernames and secret keys related to our application
pip install pytest --Package for UnitTesting
pip install django-mptt --To create Tree hierarchy in models
pip intsall drf-spectacular --To Create documentation for our API
pip install coverage --To check required tests to perform on API
pip install factory-boy --To get Replica of our original database tables

# Commands

# to create django project
django-admin startproject

# To generate custom secret key
from django.core.management.utils import get_random_secret_key
get_random_secret_key

# To run python testcase
pytest

# To generate documentation
python manage.py spectacular --file schema.yml

# To generate html Coverage file
coverage run -m pytest
