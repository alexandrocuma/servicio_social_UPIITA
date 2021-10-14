# Activate Dev Environment
- source ~/.virtualenvs/servicio/bin/activate


# Run Dev Server 
- python manage.py runserver

# Adding new models for DB 
- python manage.py makemigrations api
- python manage.py migrate

# Create and Login Admin 
- python manage.py createsuperuser

  user - servicio
  password - Servicio