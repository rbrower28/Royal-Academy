# Welcome to the Royal Academy!

Here at CODE KINGS, we value educational material and want
to give greater access to all the kingdom.

Join us on our journey to educate the world with code!

## Our Collaborators:

* Chettra Ly
* Mathieu Steele
* Daniel De La Pena Maldonado 
* Joseph Devincenzi
* Ryan Brower

## Development Environment:

* Django Python Framework
* JavaScript
* HTML & CSS

## Instructions:

Inside your environment, run this terminal command
to start a local development server:

* **python3 manage.py runserver** for MacOS
* **python manage.py runserver** for Windows

The development page will be found at this
address in your browser:

http://localhost:8000

Your changes to the code files will update when
you refresh the page on your browser.

Have fun! yes! Thanks for this!

## Further Resources:

* [Django 4.0 Documentation](https://docs.djangoproject.com/en/4.0/)
* [TutorialsPoint Django Walkthrough](https://www.tutorialspoint.com/django/index.htm)
* [W3Schools Django Resources](https://www.w3schools.com/django/index.php)

## Commands: 
* Start virual enviroment
virtualenv . or virtualenv [name of virual env]

* Activate virtualenv 
source Scripts/activate

* Install dependencies
pip install -r /path/to/requirements.txt

* syncs our settings with our django project
python manage.py migrate 

* Creates a super user you can use in the admin app and is added to the db.
python manage.py createsuperuser

* Creates custome app
python manage.py startapp [name of your app] 

* You need to run these 2 together every time you change models.py
python manage.py makemigrations
python manage.py migrate

* admin page wont work if you dont set up db

# Common Errors: 

* Model not showing in admin

If after running makemigrations and migrate the new model is not showing, check that you registered your model in the admin page of your application. 