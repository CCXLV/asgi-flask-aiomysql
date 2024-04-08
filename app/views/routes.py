import sqlalchemy as sa

from flask import Blueprint, request

from app.extensions import async_session, engine
from app.models import User

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/users', methods=['GET'])
async def get_users():
    try:
        async with async_session() as session:
            users = await session.execute(sa.select(User))
            user_instances = users.scalars().all()

            data = [user.get_data() for user in user_instances]

        await engine.dispose()
        return data, 200
    except Exception:
        await engine.dispose()
        return 'Error was occured', 400


@routes_blueprint.route('/new_user', methods=['POST'])
async def new_user():
    data = request.get_json()
    
    user = User(name=data['name'], age=data['age'])
    await user.create()

    return 'User was successfully saved', 200


@routes_blueprint.route('/user/<int:id>', methods=['GET'])
async def get_user(id):
    try:
        async with async_session() as session:
            user = await session.execute(sa.select(User).where(User.id == id))
            user_data = user.scalar().get_data()

        await engine.dispose()
        return user_data, 200
    except Exception:
        await engine.dispose()
        return 'Error was occured', 400