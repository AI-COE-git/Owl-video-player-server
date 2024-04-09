from flask import Blueprint, request

# Create a Blueprint for the count API
file_api_bp = Blueprint('file_api', __name__, url_prefix='/api/')

@file_api_bp.route('/open-file', methods=['POST'])
def open_file():
    body = request.json
    if body is None:
        return { 'error': 'No JSON data found in the request' }, 400

    file_path = body.get('file_path')
    if file_path is None:
        return { 'error': 'No "file_path" field found in the JSON data' }, 400

    return { 'file_path': file_path }

    count = 50 
    return { 'count': count }

