cd /Users/Troy/Documents/Others/Financial/financial_dash
source activate py36
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
