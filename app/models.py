import sqlalchemy as sa

from sqlalchemy.orm import DeclarativeBase
from app.extensions import async_session, engine

class BaseModel(DeclarativeBase):
       
    async def create(self):
        async with async_session() as session:
            async with session.begin():
                session.add(self)
                await session.commit()
        
        await engine.dispose()
  

    async def save(self):
        async with async_session() as session:
            async with session.begin():
                await session.commit()

        await engine.dispose()
            

    async def delete(self):
        async with async_session() as session:
            async with session.begin():
                session.delete(self)
                await session.commit()

        await engine.dispose()


class User(BaseModel):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(64))
    age = sa.Column(sa.Integer)

    def get_data(self):
        data = {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

        return data