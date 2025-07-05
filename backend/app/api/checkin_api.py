from flask_restx import Namespace, Resource, fields
from flask_login import current_user, login_required
from app.extensions import db
from app.models import Checkin

checkin_ns = Namespace('checkin', description='Check-in operations')

checkin_model = checkin_ns.model('Checkin', {
    'id': fields.Integer(readOnly=True, description='Check-in ID'),
    'habit_id': fields.Integer(required=True, description='Habit ID'),
    'date': fields.Date(required=True, description='Check-in date'),
    'status': fields.String(required=True, description='Status of the check-in'),
})


@checkin_ns.route('/')
class CheckinList(Resource):
    @checkin_ns.marshal_with(checkin_model)
    @login_required
    def get(self):
        checkins = Checkin.query.filter_by(user_id=current_user.id).all()
        return checkins

    @checkin_ns.expect(checkin_model)
    @checkin_ns.marshal_with(checkin_model, code=201)
    @login_required
    def post(self):
        data = checkin_ns.payload
        new_checkin = Checkin(
            user_id=current_user.id,
            habit_id=data['habit_id'],
            timestamp=data['timestamp']
        )
        db.session.add(new_checkin)
        db.session.commit()
        return new_checkin, 201


@checkin_ns.route('/<int:id>')
@checkin_ns.param('id', 'Check-in ID')
@checkin_ns.response(404, 'Check-in not found')
class CheckinResource(Resource):
    @checkin_ns.marshal_with(checkin_model)
    @login_required
    def get(self, id):
        checkin = Checkin.query.filter_by(id=id, user_id=current_user.id).first()
        if checkin is None:
            checkin_ns.abort(404, f'Check-in {id} not found')
        return checkin

    @checkin_ns.expect(checkin_model)
    @checkin_ns.marshal_with(checkin_model)
    @login_required
    def put(self, id):
        data = checkin_ns.payload
        checkin = Checkin.query.filter_by(id=id, user_id=current_user.id).first()
        if checkin is None:
            checkin_ns.abort(404, f'Check-in {id} not found')
        checkin.habit_id = data['habit_id']
        checkin.timestamp = data['timestamp']
        db.session.commit()
        return checkin

    @login_required
    def delete(self, id):
        checkin = Checkin.query.filter_by(id=id, user_id=current_user.id).first()
        if checkin is None:
            checkin_ns.abort(404, f'Check-in {id} not found')
        db.session.delete(checkin)
        db.session.commit()
        return '', 204
