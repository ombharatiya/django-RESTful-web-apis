# django-RESTful-web-apis

**In this project we have created e-commercial site's RESTful back-end APIs using Django REST framework.**

We have used following concepts of Django & DRF to complete this project:

- Serializer
- API views
- Django filters - filtering back ends
- Pagination, search, listing & custom query etc.
- Routers with viewsets
- Executing CRUD operations
- Managing serializer fields
- Testing API views
- data-driven web experiences

To setup the project:

```

$ git clone https://github.com/ombharatiya/django-RESTful-web-apis.git
$ cd django-RESTful-web-apis
$ vrtualenv -p python3.6 .venv
$ source .venv/bin/activate
<.venv>$ pip install -r requirements.txt
<.venv>$ python manage.py runserver

```
Now you can check various apis on http://localhost:8000

To run it on '127.0.0.1', you might be required to add this host in settings.py file ALLOWED_HOSTS = ['127.0.0.1'] or do ALLOWED_HOSTS = ['\*'] .

