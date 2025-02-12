#### Django Class By Technology Channel

### Introduction
Django is high level Python web development framework 
that helps fast development of secure and maintainable website.

### Advantage:
- Fast
- Secure
- Scalable


### Already Build With Django
- Instagram, nationalgeographic, pinterest, Khalti, Mozilla



### Django Use MVT 
Model: Data Structure
View: Logic From Model and render to template 
Template: Presentation where data is displayed to user.


### Why Django?
- All things included [Batteries Included] [Built In]
- DRY [Don't Repeat Yourself]
- Community Support


### Django Alternatives
1. Flask [Lightweight but need more configuration]
2. Laravel
3. Ruby on Rails [Based on Ruby Programming Language]


### Requirements Install
1. Python 
2. virtualenv
```bash
pip install virtualenv
```
To create virutal env
```bash
virtualenv myenv
```
Activate using bash
```bash
source myenv/Scripts/activate
```

```bash
pip install Django
```

3. Vs Code

Optional
- Chrome Extension For Django


### How to Create First Project
Go to virtual env and run this command.\
```bash
django-admin startproject myweekroutine
```
### Run Project
```bash
python manage.py runserver 
```

### Run on Different Port
```bash
python manage.py runserver 8181
```


### Project File Structure
**manage.py** - A utility for interacting with Django project from command.

### Inside myproject
**settings.py** - Setting files for your project.
**urls.py** - Define URL routing for project.
**__init__.py** - Marks this directory as python package.
**asgi.py** Configuration for ASGI [Asynchronous Server Gateway Interface]
- **wsgi.py** - Configuration for WSGI [Web Server GateWay Interface]
-- **db.sqlite** - Default SQlite database


### Django App
Django app is web application that does one thing. For e.g. blog, ecommerce, forum, etc.
- Django project can contain multiple apps.
- Apps are reusable

### How to Create Django App
```bash
python manage.py startapp <appname>
```

### Project Vs App
- **Project** is overall configuration that ties multiple apps together.

- **App** is independent module/feature of project.


### Inside App
**__init__.py** - Marks this directory as python package.
**admin.py** - Register models to apprear on Django admin interface.
**apps.py** - Contain the configuration for app.
**models.py** - Define Database models.
**tests.py** - Used to write unit test for app.
**views.py** - Logic for handling request and returning response.
**migrations/**- Contains migration files for database changes.



### Connect App to Project
- Open settings.py and find INSTALLED_APPS list.
- Add your new app to the list.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]
```


### URL
Define URL routing for project.
- https://technologychannel.org/ - Root URL
- https://technologychannel.org/about/ - About URL

### Views
Logic for handling request and returning response. It can be function or class.


### Tasks
- Create Project **myproject** and create app **myapp**. Define 5 urls
1. / - It should display message 'Welcome to Home'
2. /contact - It should display message 'Welcome to Contact'
3. /about - It should display message 'Welcome to About'
4. /service - It should display message 'Welcome to Service'
5. /skill - It should display message 'Welcome to Skill'