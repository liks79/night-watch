import redis
import psycopg2
import datetime
from psycopg2 import OperationalError, errorcodes, errors
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException
from starlette.requests import Request
from config import settings, logger


app = FastAPI(title=settings.app_title,
              description=settings.app_description,
              version=settings.app_version)


@app.get('/redis/health')
async def redis_health_check(request: Request):
    try:
        r = redis.from_url(settings.redis_url)
        r.set(settings.redis_key, settings.redis_key, datetime.timedelta(seconds=60*60))
        r.get(settings.redis_key)
        r.close()
        return {'Hello': 'Redis'}
    except redis.RedisError:
        logger.error(f'path={request.url.path} : Failed')
        raise HTTPException(
            status_code=500,
            detail='Redis health check failed',
            headers={'X-Error': 'There goes Redis error'},
        )


@app.get('/postgresql/health')
async def postgresql_health_check(request: Request):
    try:
        connection = psycopg2.connect(settings.db_conn)
        cur = connection.cursor()
        cur.execute(settings.db_check_sql)
        cur.close()
        return {'Hello': 'Postgresql'}

    except OperationalError as err:
        logger.error(f'path={request.url.path} : Failed')
        raise HTTPException(
            status_code=500,
            detail='Postgresql health check failed',
            headers={'X-Error': 'There goes Postgresql error'},
        )
