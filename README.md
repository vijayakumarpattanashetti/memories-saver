# Memories Saver, Django Rest  API Framework based CRUD app


## Setup

1) Create the project directory and start virtual environment.
2) Refer to requirements.txt, and install the requirements.
3) Copy all the files/clone this repo.
4) Run -
  a) python manage.py makemigrations api
  b) python manage.py migrate
  c) python manage.py runserver
5) Create admin: python manage.py createsuperuser
6) Add some users to play with.


## Testing

1) Run: python tests.py
2) Open localhost:8000
  a) / : home page
  b) /auth/login/: login page
  b) /memories/ : lists current data, post user login
  c) play around 
     i) Fill "Text" and click "POST" to Create
     b) GET with /memories/<id>/ to Read
     c) Update "Text" and click "PUT" to Update
     d) Click DELETE to Delete
2) Postman: Use urls and provide necessary Auth & Body, and validate previously tested CRUD actions
   *Base URL: localhost:8000 or https://memories-saver.herokuapp.com (deployed on heroku by me)


## Before deploying on production site

1) Run: python manage.py check --debug
2) Make sure nothing is returned, till then keep clearing all the warnings
