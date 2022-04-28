# RequestApiLogging
Django logging query api

# Requirements
* [python 3.6.x](https://www.python.org/) or higher (pip also come with python 3.4.x or higher)
* [pandas 1.1.1](https://pypi.org/project/pandas/1.1.1/) or higher
* [Django 3.2.x](https://www.djangoproject.com/)

# Setting Up
### Project
- Create ReqeustLog models for keep log query api (Ref. /log/models.py)
- Copy and modify Middleware script to main project (ex. django-logging-query/django_logging/middleware.py)
- Add 2 class in Middleware script to middleware in main project setting


    middle = [
    ...,
    'django_logging.middleware.RequestMiddleware',
    'django_logging.middleware.LoggingMiddleware',
    ...
    ]