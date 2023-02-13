#!/usr/bin/env python3
""" Module of Session authentication views """
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - the User ID or None
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            session_name = getenv('SESSION_NAME')
            response = jsonify(user.to_json())
            response.set_cookie(session_name, session_id)
            return response
        else:
            return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    Return:
      - True if the user is logged out, otherwise False
    """
    destroy_session = auth.destroy_session(request)
    if destroy_session is False:
        abort(404)
    else:
        return jsonify({}), 200
