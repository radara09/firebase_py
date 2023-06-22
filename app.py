from flask import Flask, render_template, request
from crud_operations import create_data, read_data, update_data, delete_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    data = request.form.to_dict()
    create_data('collection_name', data)
    return 'Data created successfully!'

@app.route('/read', methods=['GET'])
def read():
    read_data('collection_name')
    return 'Data retrieved successfully!'

@app.route('/update', methods=['PUT'])
def update():
    data = request.form.to_dict()
    document_id = data['document_id']
    del data['document_id']
    update_data('collection_name', document_id, data)
    return 'Data updated successfully!'

@app.route('/delete', methods=['DELETE'])
def delete():
    document_id = request.args.get('document_id')
    delete_data('collection_name', document_id)
    return 'Data deleted successfully!'

if __name__ == '__main__':
    app.run()
