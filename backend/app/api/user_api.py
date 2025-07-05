from flask_restx import Namespace, Resource, fields
from flask_login import current_user, login_required
from app.extensions import db

user_ns = Namespace('user', description='User operations')

user_model = user_ns.model('User', {
    'id': fields.Integer(readOnly=True, description='User ID'),
    'username': fields.String(required=True, description='The username of the user'),
    'email': fields.String(required=True, description='The email of the user'),
    'created_at': fields.DateTime(description='Creation timestamp'),
    'updated_at': fields.DateTime(description='Last update timestamp')
})


@user_ns.route('/me')
class UserResource(Resource):
    @user_ns.marshal_with(user_model)
    @login_required
    def get(self):
        """Get the current user's information."""
        return current_user

    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model)
    @login_required
    def put(self):
        """Update the current user's information."""
        data = user_ns.payload
        current_user.username = data['username']
        current_user.email = data['email']
        db.session.commit()
        return current_user
