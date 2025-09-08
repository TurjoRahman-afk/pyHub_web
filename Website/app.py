from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import io

app = Flask(__name__)
CORS(app)

# In-memory user store with solved problems
users = {}  # {username: {"password": ..., "solvedProblems": [...] }}

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
    users[username] = {"password": password, "solvedProblems": []}
    return jsonify({'success': True})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    user = users.get(username)
    if user and user["password"] == password:
        return jsonify({
            'success': True,
            'username': username,
            'solvedProblems': user["solvedProblems"]
        })
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password.'})

@app.route('/api/userinfo', methods=['GET'])
def userinfo():
    username = request.args.get('username', '').strip()
    user = users.get(username)
    if user:
        return jsonify({
            'username': username,
            'solvedProblems': user["solvedProblems"]
        })
    else:
        return jsonify({'username': '', 'solvedProblems': []})

@app.route('/api/solve', methods=['POST'])
def solve_problem():
    data = request.json
    username = data.get('username', '').strip()
    problem_id = data.get('problem_id')
    user = users.get(username)
    if user and problem_id is not None:
        if problem_id not in user["solvedProblems"]:
            user["solvedProblems"].append(problem_id)
        return jsonify({'success': True, 'solvedProblems': user["solvedProblems"]})
    return jsonify({'success': False, 'message': 'Invalid user or problem.'})

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