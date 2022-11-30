# random-quotes-python-api
## Description:
It is a django restframework project consists of two main apps :
quotes & account.There are endpoints you can check them from postman collections.
Fixtures were used to load data from json file to django orm .
XlsxWriter package used to write excel file that shows the quote report.
## Installation:
#### Installing Prerequisites:
`sudo apt update `
`sudo apt install python3-dev `
`python3-venv`
`python3-django -y`
#### Setting up development environment:


to install enivronment:

    `python3 -v venv random_quote_env`
    `python3 -m venv random_quote_env`

to Activate Environment:

    `source random_quote-env/bin/activate`
to install django as a local pacakge inside the environment:

   `pip install django`

to install django restframework:

 `pip install djangorestframework`

to install django database dependpendcies:

`pip install django-extensions`

to run database :

   `python manage.py makemigrations`

   `python manage.py migrate`

to create admin:

`manage.py createsuperuser`

install packages :

`pip install xlsxwriter`

load quotes data from fixtures:

`python manage.py loaddata quotes`

load authors data from fixtures:

`python manage.py loaddata authors`

#### Run server:
`python manage.py runserver`


## Postman Collection 
[Postman collection](https://drive.google.com/file/d/1dkxjFgkJGOyhDdrZ0Rpxa07oNMYfqyRs/view?usp=sharing)