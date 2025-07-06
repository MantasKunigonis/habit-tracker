from flask_restx import Namespace, Resource, fields
from flask_login import current_user, login_required
from app.extensions import db
from app.models import Checkin

checkin_ns = Namespace('checkin', description='Check-in operations')

checkin_model = checkin_ns.model('Checkin', {
    'id': fields.Integer(readOnly=True, description='Check-in ID'),
    'habit_id': fields.Integer(required=True, description='Habit ID'),
    'user_id': fields.Integer(required=True, description='User ID'),
    'status': fields.String(required=True, description='Status of the check-in'),
    'timestamp': fields.DateTime(required=True, description='Check-in timestamp')
})


@checkin_ns.route('/')
class CheckinList(Resource):
    @checkin_ns.marshal_with(checkin_model, code=200)
    @checkin_ns.response(200, 'Check-ins retrieved successfully')
    @login_required
    def get(self):
        """Get all check-ins for the current user."""
        checkins = Checkin.query.filter_by(user_id=current_user.id).all()
        return checkins, 200

    @checkin_ns.marshal_with(checkin_model, code=201)
    @checkin_ns.expect(checkin_model)
    @checkin_ns.response(201, 'Check-in created successfully')
    @login_required
    def post(self):
        """Create a new check-in for a habit."""
        data = checkin_ns.payload
        new_checkin = Checkin(
            habit_id=data['habit_id'],
            user_id=current_user.id,
            status=data['status']
        )
        db.session.add(new_checkin)
        db.session.commit()
        return new_checkin, 201


@checkin_ns.route('/<int:id>')
@checkin_ns.param('id', 'Check-in ID')
class CheckinResource(Resource):
    @checkin_ns.marshal_with(checkin_model, code=200)
    @checkin_ns.response(200, 'Check-in retrieved successfully')
    @checkin_ns.response(404, 'Check-in not found')
    @login_required
    def get(self, id):
        """Get a specific check-in by ID."""
        checkin = Checkin.query.filter_by(id=id, user_id=current_user.id).first()
        if checkin is None:
            checkin_ns.abort(404, f'Check-in {id} not found')
        return checkin, 200

    @checkin_ns.expect(checkin_model)
    @checkin_ns.marshal_with(checkin_model, code=200)
    @checkin_ns.response(200, 'Check-in updated successfully')
    @checkin_ns.response(404, 'Check-in not found')
    @login_required
    def put(self, id):
        """Update a specific check-in by ID."""
        data = checkin_ns.payload
        checkin = Checkin.query.filter_by(id=id, user_id=current_user.id).first()
        if checkin is None:
            checkin_ns.abort(404, f'Check-in {id} not found')
        checkin.habit_id = data['habit_id']
        db.session.commit()
        return checkin, 200

    @checkin_ns.response(204, 'Check-in deleted successfully')
    @checkin_ns.response(404, 'Check-in not found')
    @login_required
    def delete(self, id):
        """Delete a specific check-in by ID."""
        checkin = Checkin.query.filter_by(id=id, user_id=current_user.id).first()
        if checkin is None:
            checkin_ns.abort(404, f'Check-in {id} not found')
        db.session.delete(checkin)
        db.session.commit()
        return {'message': 'Check-in deleted successfully'}, 204
