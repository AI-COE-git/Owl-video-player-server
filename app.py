from flask import Flask
from routes.block_count_api import block_count_api_bp  # Import the Blueprint
from routes.file_api import file_api_bp  # Import the Blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api*": {"origins": "http://localhost:*"}})

# Register the block count API Blueprint
app.register_blueprint(block_count_api_bp)
app.register_blueprint(file_api_bp)

@app.route('/')
def hello():
    return 'Hello, welcome to the video-player-server!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
