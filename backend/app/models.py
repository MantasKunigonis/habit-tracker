from app.extensions import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    # Auto-incrementing unique identifier for each user
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    # Unique username for user identification
    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    # Unique email for user identification
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )
    # Hashed password for security
    password_hash = db.Column(
        db.String(128),
        nullable=False
    )
    # Timestamp for when the user was created
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp()
    )
    # Timestamp for when the user was last updated
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )
    # One-to-many relationship with Habit
    habits = db.relationship(
        'Habit',
        backref='user',
        lazy=True
    )


class Habit(db.Model):
    # Auto-incrementing unique identifier for each habit
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    # Foreign key to link to User
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    # Name of the habit
    name = db.Column(
        db.String(100),
        nullable=False
    )
    # Optional description of the habit
    description = db.Column(
        db.String(255),
        nullable=True
    )
    # Timestamp for when the habit was created
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp()
    )
    # Timestamp for when the habit was last updated
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )
    # One-to-many relationship with Checkin
    checkins = db.relationship(
        'Checkin',
        backref='habit',
        lazy=True
    )


class Checkin(db.Model):
    # Auto-incrementing unique identifier for each check-in
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    # Foreign key to link to Habit
    habit_id = db.Column(
        db.Integer,
        db.ForeignKey('habit.id'),
        nullable=False
    )
    # Date of the check-in
    date = db.Column(
        db.Date,
        nullable=False
    )
    # Status of the check-in (e.g., 'done', 'missed')
    status = db.Column(
        db.String(20),
        nullable=False
    )
