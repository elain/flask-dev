 virtualenv venv
 source venv/bin/activate

pip install -r requirements.txt

 python manage.py test
 python manage.py db upgrade
 python manage.py runserver
