from flask_restx import Namespace, Resource, fields
from flask import request
from app.models import User
from app.extensions import db
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash


auth_ns = Namespace('auth', description='Authentication operations')

user_model = auth_ns.model('User', {
    'username': fields.String(required=True, description='The username of the user'),
    'email': fields.String(required=True, description='The email of the user'),
    'password': fields.String(required=True, description='The password of the user')
})

login_model = auth_ns.model('Login', {
    'username': fields.String(required=True, description='The username of the user'),
    'password': fields.String(required=True, description='The password of the user')
})


@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.expect(user_model)
    @auth_ns.doc(description="Register endpoint that creates a new user.")
    @auth_ns.response(201, 'User registered successfully')
    @auth_ns.response(400, 'User already exists')
    def post(self):
        """Register a new user."""
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return {'message': 'Username already exists'}, 400
        if User.query.filter_by(email=data['email']).first():
            return {'message': 'Email already exists'}, 400
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=generate_password_hash(data['password'])
        )
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User registered successfully'}, 201


@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    @auth_ns.response(200, 'Login successful')
    @auth_ns.response(401, 'Invalid credentials')
    def post(self):
        """Log in a user."""
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return {'message': 'Login successful'}, 200
        return {'message': 'Invalid credentials'}, 401


@auth_ns.route('/logout')
class Logout(Resource):
    @login_required
    @auth_ns.response(200, 'Logout successful')
    def post(self):
        """Log out the current user."""
        logout_user()
        return {'message': 'Logout successful'}, 200
