# Packages

pip install django
pip install djangorestframework
pip install python-dotenv --To store the passwords and usernames and secret keys related to our application
pip install pytest --Package for UnitTesting
pip install django-mptt --To create Tree hierarchy in models

# Commands

# to create django project
django-admin startproject

# To generate custom secret key
from django.core.management.utils import get_random_secret_key
get_random_secret_key

# To run python testcase
pytest
