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

- PIP Dependencies

asgiref==3.3.4
CacheControl==0.12.6
cachetools==4.2.2
certifi==2021.5.30
cffi==1.14.5
chardet==4.0.0
Django==3.2.4
django-filter==2.4.0
djangorestframework==3.12.4
firebase-admin==5.0.1
google-api-core==1.30.0
google-api-python-client==2.10.0
google-auth==1.32.0
google-auth-httplib2==0.1.0
google-cloud-core==1.7.0
google-cloud-firestore==2.1.3
google-cloud-storage==1.39.0
google-crc32c==1.1.2
google-resumable-media==1.3.1
googleapis-common-protos==1.53.0
grpcio==1.38.1
httplib2==0.19.1
idna==2.10
Markdown==3.3.4
msgpack==1.0.2
packaging==20.9
proto-plus==1.18.1
protobuf==3.17.3
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.20
pyparsing==2.4.7
pytz==2021.1
requests==2.25.1
rsa==4.7.2
six==1.16.0
sqlparse==0.4.1
uritemplate==3.0.1
urllib3==1.26.5