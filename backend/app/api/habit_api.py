from flask_restx import Namespace, Resource, marshal_with, fields
from app.models import Habit
from flask_login import current_user, login_required
from flask import request
from app.extensions import db

habit_ns = Namespace('habits', description='Habit related operations')


habit_model = habit_ns.model('Habit', {
    'id': fields.Integer(required=True, description='Habit ID'),
    'user_id': fields.Integer(required=True, description='User ID'),
    'name': fields.String(required=True, description='Habit name'),
    'description': fields.String(description='Habit description'),
    'created_at': fields.DateTime(description='Creation timestamp'),
    'updated_at': fields.DateTime(description='Last update timestamp')
})


@habit_ns.route('/')
class HabitList(Resource):
    @habit_ns.response(200, 'Success')
    @marshal_with(habit_model, as_list=True)
    @login_required
    def get(self):
        habits = Habit.query.filter_by(user_id=current_user.id).all()
        return habits

    @habit_ns.expect(habit_model)
    @habit_ns.response(201, 'Habit created')
    @login_required
    def post(self):
        data = request.get_json()
        new_habit = Habit(
            user_id=current_user.id,
            name=data['name'],
            description=data.get('description'),
        )
        db.session.add(new_habit)
        db.session.commit()
        return new_habit.to_dict(), 201


@habit_ns.route('/<int:id>')
@habit_ns.param('id', 'Habit ID')
@habit_ns.response(404, 'Habit not found')
class HabitResource(Resource):
    @marshal_with(habit_model)
    @login_required
    def get(self, id):
        habit = Habit.query.get(id)
        if habit is None:
            habit_ns.abort(404, f'Habit {id} not found')
        return habit
