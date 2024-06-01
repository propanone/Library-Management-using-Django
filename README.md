# how to run : 
 1. install django :
  ```bash
  python -m pip install Django
  ```
2. update models of db :
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
3. (optional) change the port and ip addr
```bash
python manage.py runserver 0.0.0.0:8000
```

#  db :
1. to reset counters and history : 
```bash
python manage.py  makemigrations --empty lib_sys_app
```
2. delete db content :
```bash
python manage.py  shell
```
```bash
from lib_sys_app.models import book
book.objects.all().delete()
```
3. upload a db : 
visit : http://127.0.0.1:8000/upload
upload the csv provided or your own csv

# How to create a django app : 
1. create the projcet : modify settings 
```
django-admin startproject mysite
```
output:   mysite/
          manage.py
          mysite/
              __init__.py
              settings.py
              urls.py
              asgi.py
              wsgi.py

2. create your app : 
```
python manage.py startapp polls
```
output:   polls/
          __init__.py
          admin.py
          apps.py
          migrations/
              __init__.py
          models.py
          tests.py
          views.py

2. run server :
```
python manage.py runserver
```
3. update models :
```
python manage.py migrate
```
```
python manage.py makemigrations polls
```

4.create an admin :
```
python manage.py createsuperuser
```
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
run : 
```
python manage.py runserver
```
to access the admin page visit eg. : http://127.0.0.1:8000/admin/

 ![admin01](https://github.com/propanone/MiniProject/assets/110060901/ee0daa36-d498-4024-bfd7-1b324e8ba912)
