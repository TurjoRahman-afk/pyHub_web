from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import io

app = Flask(__name__)
CORS(app)

users = {}  # In-memory user store

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password are required.'})
    if len(username) > 8 or len(password) > 8:
        return jsonify({'success': False, 'message': 'Username and password must be under 8 characters.'})
    if username in users:
        return jsonify({'success': False, 'message': 'Username already exists.'})
    users[username] = password
    return jsonify({'success': True})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    if users.get(username) == password:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password.'})

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    output = io.StringIO()
    try:
        sys.stdout = output
        exec(code, {})
        sys.stdout = sys.__stdout__
        return jsonify({'output': output.getvalue()})
    except Exception as e:
        sys.stdout = sys.__stdout__
        return jsonify({'output': str(e)})

if __name__ == '__main__':
    app.run(debug=True)