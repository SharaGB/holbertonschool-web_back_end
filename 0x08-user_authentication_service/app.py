#!/usr/bin/env python3
""" FLASK module """
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """ Index """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """ Users """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ Function to respond to the POST /sessions route """
    email = request.form.get('email')
    password = request.form.get('password')
    valid_login = AUTH.valid_login(email, password)

    if valid_login:
        session_id = AUTH.create_session(email)
        msg = {"email": "<user email>", "message": "logged in"}
        response = jsonify(msg)
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ Logout function """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ Profile function """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ Get reset password token """
    try:
        email = request.form.get('email')
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ Update password """
    email = request.form.get('email')
    token = request.form.get('reset_token')
    pwd = request.form.get('new_password')
    try:
        AUTH.update_password(token, pwd)
    except Exception:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
