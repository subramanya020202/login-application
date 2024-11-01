from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

users = {
    "user1": "password123",
    "user2": "password456"
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True, host ="0.0.0.0")

