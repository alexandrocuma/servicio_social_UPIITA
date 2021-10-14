import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("firebase/servicio.json")


def init_firebase(url="https://ejemploku-default-rtdb.firebaseio.com"):
    print(firebase_admin._apps)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            'databaseURL': url
        })
