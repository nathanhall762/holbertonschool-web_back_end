#!/usr/bin/env python3
from auth import Auth
from flask import Flask, jsonify, request, abort, redirect

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def index():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        if session_id:
            response = jsonify({'email': email, 'message': 'logged in'})
            response.set_cookie('session_id', session_id)
            return response
        else:
            abort(500)  # Failed to create a session
    else:
        abort(401)  # Incorrect login information


@app.route('/sessions', methods=['DELETE'])
def logout():
    session_id = request.cookies.get('session_id')

    if session_id:
        user = AUTH.get_user_from_session_id(session_id)

        if user:
            AUTH.destroy_session(user.id)
            return redirect('/')
        else:
            abort(403)  # User with session ID not found
    else:
        abort(403)  # No session ID provided


@app.route('/profile', methods=['GET'])
def profile():
    session_id = request.cookies.get('session_id')

    if session_id:
        user = AUTH.get_user_from_session_id(session_id)

        if user:
            return jsonify({"email": user.email}), 200
        else:
            abort(403)  # User with session ID not found
    else:
        abort(403)  # No session ID provided


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
