from .extensions import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(
        db.Integer,
        primary_key=True
    )  # Auto-incrementing unique identifier for each user
    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )  # Unique username for user identification
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )  # Unique email for user identification
    password_hash = db.Column(
        db.String(128),
        nullable=False
    )  # Hashed password for security
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp()
    )  # Timestamp for when the user was created
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )  # Timestamp for when the user was last updated
    habits = db.relationship(
        'Habit',
        backref='user',
        lazy=True
    )  # One-to-many relationship with Habit


class Habit(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )  # Auto-incrementing unique identifier for each habit
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )  # Foreign key to link to User
    name = db.Column(
        db.String(100),
        nullable=False
    )  # Name of the habit
    description = db.Column(
        db.String(255),
        nullable=True
    )  # Optional description of the habit
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp()
    )  # Timestamp for when the habit was created
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )  # Timestamp for when the habit was last updated
    checkins = db.relationship(
        'Checkin',
        backref='habit',
        lazy=True
    )  # One-to-many relationship with Checkin


class Checkin(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )  # Auto-incrementing unique identifier for each check-in
    habit_id = db.Column(
        db.Integer,
        db.ForeignKey('habit.id'),
        nullable=False
    )  # Foreign key to link to Habit
    date = db.Column(
        db.Date,
        nullable=False
    )  # Date of the check-in
    status = db.Column(
        db.String(20),
        nullable=False
    )  # Status of the check-in (e.g., 'done', 'missed')
