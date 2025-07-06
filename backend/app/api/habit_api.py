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
    @marshal_with(habit_model)
    @habit_ns.response(200, 'Habits retrieved successfully')
    @login_required
    def get(self):
        """Get all habits for the current user."""
        habits = Habit.query.filter_by(user_id=current_user.id).all()
        return habits, 200

    @marshal_with(habit_model)
    @habit_ns.expect(habit_model)
    @habit_ns.response(201, 'Habit created successfully')
    @login_required
    def post(self):
        """Create a new habit for the current user."""
        data = request.get_json()
        new_habit = Habit(
            user_id=current_user.id,
            name=data['name'],
            description=data.get('description'),
        )
        db.session.add(new_habit)
        db.session.commit()
        return new_habit, 201


@habit_ns.route('/<int:id>')
@habit_ns.param('id', 'Habit ID')
class HabitResource(Resource):
    @marshal_with(habit_model)
    @habit_ns.response(200, 'Habit retrieved successfully')
    @habit_ns.response(404, 'Habit not found')
    @login_required
    def get(self, id):
        """Get a specific habit by ID."""
        habit = Habit.query.get(id)
        if habit is None:
            habit_ns.abort(404, f'Habit {id} not found')
        return habit, 200

    @marshal_with(habit_model)
    @habit_ns.expect(habit_model)
    @habit_ns.response(200, 'Habit updated successfully')
    @habit_ns.response(404, 'Habit not found')
    @login_required
    def put(self, id):
        """Update a specific habit by ID."""
        data = request.get_json()
        habit = Habit.query.get(id)
        if habit is None:
            habit_ns.abort(404, f'Habit {id} not found')
        habit.name = data['name']
        habit.description = data.get('description', habit.description)
        db.session.commit()
        return habit, 200

    @habit_ns.response(204, 'Habit deleted successfully')
    @habit_ns.response(404, 'Habit not found')
    @login_required
    def delete(self, id):
        """Delete a specific habit by ID."""
        habit = Habit.query.get(id)
        if habit is None:
            habit_ns.abort(404, f'Habit {id} not found')
        db.session.delete(habit)
        db.session.commit()
        return {'message': 'Habit deleted successfully'}, 204
