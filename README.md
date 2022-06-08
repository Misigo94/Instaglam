Instagram
AA project that ahs cloned the instagrm application that allowd the users to view and like comment on other peoples 

Author
Martin Misigo
Getting Started
Fork this repository or clone it to your local machine running Ubuntu by using the following commands:

git clone https://github.com/Misigo94/Instaglam.git
Prerequisites
You will need to be running the following:

Python version 3.9
postgres database
Installing
A step by step series of examples that tell you how to get a development env running

set up a virtual environment using the following command
python3.9 -m venv --without-pip virtual
And activate it

source virtual/bin/activate
install the latest version of pip
curl https://bootstrap.pypa.io/get-pip.py | python
Install the requirements in the requirements.txt file using
pip install -r requirements.txt
create a .env file in your rootfolder and add the following configurations
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
create postgres database
CREATE DATABASE <your-database-name>
create a migration using the following command
python3.9 manage.py makemigrations
and migrate

python3.9 manage.py migrate
create an admin account
python 3.9 manage.py createsuperuser
and fill-in your credentials

run the application using
python3.9 manage.py runserver
navigate to the admin panel by typing
localhost:8000/admin
Running the tests
Run the following commands:

python3.9 manage.py tests
Deployment
View the following document inorder to deploy to a live system

Built Using
Django
Bootstrap
MDBootstrap
Html
Python
Contact Info
Phone: 0715700355
Email: misigomartin@gmail.com
License
This project is licensed under the MIT License - see the LICENSE file for details