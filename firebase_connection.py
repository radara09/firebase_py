import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firestore():
    cred = credentials.Certificate("key.json")
    firebase_admin.initialize_app(cred)

def get_firestore_db():
    db = firestore.client()
    return db
