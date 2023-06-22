from firebase_connection import get_firestore_db

def create_data(collection_name, data):
    db = get_firestore_db()
    db.collection(collection_name).add(data)

def read_data(collection_name):
    db = get_firestore_db()
    docs = db.collection(collection_name).get()
    for doc in docs:
        print(doc.to_dict())

def update_data(collection_name, document_id, data):
    db = get_firestore_db()
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.update(data)

def delete_data(collection_name, document_id):
    db = get_firestore_db()
    doc_ref = db.collection(collection_name).document(document_id)
    doc_ref.delete()
