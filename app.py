from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # Process the file (you can add your Excel processing logic here)
    return jsonify({"message": "File processed"})

if __name__ == '__main__':
    app.run()
