from flask_restx import Api
from app.api.auth_api import auth_ns
from app.api.user_api import user_ns
from app.api.habit_api import habit_ns
from app.api.checkin_api import checkin_ns

api = Api(
    title='Habit Tracker API',
    version='1.0',
    description='API for tracking user habits',
    doc='/docs'
)

api.add_namespace(auth_ns, path='/api/auth')
api.add_namespace(user_ns, path='/api/user')
api.add_namespace(habit_ns, path='/api/habit')
api.add_namespace(checkin_ns, path='/api/checkin')
