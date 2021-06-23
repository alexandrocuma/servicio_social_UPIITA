from firebase_admin import db


def get_data_from(path="/"):
    ref = db.reference(path)
    print(ref.get())


def insert_data_to(path="/"):
    ref = db.reference(path)
    print(ref.push({
        "test": "test"
    }))
