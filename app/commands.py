import asyncio
import click

from flask.cli import with_appcontext

from app.models import BaseModel
from app.extensions import engine


@click.command('init_db')
@with_appcontext
def init_db():
    click.echo('Database is being created...')

    asyncio.get_event_loop().run_until_complete(_init_db_async())

    click.echo('Database was created!')

async def _init_db_async():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)