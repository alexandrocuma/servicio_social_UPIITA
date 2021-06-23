import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("firebase/servicio.json")


def init_firebase():
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://ejemploku-default-rtdb.firebaseio.com'
    })
