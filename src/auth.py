import validators as validators
from src.constants.http_status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_201_CREATED
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from src.database import User, db

auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth.post("/register")
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if len(password) < 6:
        return jsonify({
            'error': 'Password is too short'
        }), HTTP_400_BAD_REQUEST

    if len(username) < 6:
        return jsonify({
            'error': 'Username is too short'
        }), HTTP_400_BAD_REQUEST

    if not username.isalnum() or " " in username:
        return jsonify({
            'error': 'Username should be alphanumeric, also no spaces'
        }), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({
            'error': 'Email is not valid'
        }), HTTP_400_BAD_REQUEST

    if User.query.filter_by(email=email).first() is not None:
        return jsonify({
            'error': 'Email is taken'
        }), HTTP_409_CONFLICT

    pwd_hash = generate_password_hash(password)
    user = User(username=username, password=pwd_hash, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': 'User created',
        'user': {
            'username': username,
            'email': email
        }
    }), HTTP_201_CREATED


@auth.get("/me")
def me():
    return {"user": "me"}
