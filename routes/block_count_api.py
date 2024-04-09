from flask import Blueprint, request
import time
import random

# Create a Blueprint for the count API
block_count_api_bp = Blueprint('block_count_api', __name__, url_prefix='/api')

@block_count_api_bp.route('/set-start', methods=['POST'])
def set_start():
    body = request.json
    if body is None:
        return { 'error': 'No JSON data found in the request' }, 400

    frame_number = body.get('frameNumber')
    if frame_number is None:
        return { 'error': 'No "frameNumber" field found in the JSON data' }, 400

    return { 'frameNumber': frame_number }

@block_count_api_bp.route('/set-end', methods=['POST'])
def set_end():
    body = request.json
    if body is None:
        return { 'error': 'No JSON data found in the request' }, 400

    frame_number = body.get('frameNumber')
    if frame_number is None:
        return { 'error': 'No "frameNumber" field found in the JSON data' }, 400

    return { 'frameNumber': frame_number }

@block_count_api_bp.route('/get-count', methods=['GET'])
def get_count():
    time.sleep(2)
    countLeft = random.randint(1, 150)
    countRight = random.randint(1, 150)
    return { 'countLeft': countLeft, 'countRight': countRight }

