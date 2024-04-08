import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

load_dotenv('secrets.env')

engine = create_async_engine(os.getenv('MYSQL_URL'))
async_session = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)