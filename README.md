# BeatShop

Application created in Django rest framework and vue.
To run the API you need to makemigrations in django project by running these commands:
```
python manage.py makemigrations
python manage.py migrate
```
To run front end you need to have vue installed, then in beathshop_vue run command:
```
npm run serve
```
You also need to add two files:

beatshop//beathsop/private.py
```
SECRET_KEY = 'django secret key'
STRIPE_SECRET_KEY = 'stripe secret key'
```
beatshop_vue/src/private.js
```
export const stripe_secret_key = 'stripe secret key';
```
Now you can finnaly run API server:

python manage.py runserver
