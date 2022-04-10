import os
import sys
import logging
from pydantic import BaseSettings

logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stderr)
streamHandler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(streamHandler)


class Settings(BaseSettings):

    app_title: str = 'statping_backend_watcher.'
    app_description: str = 'Monitoring Elasticache and Postgresql.'
    app_version: str = 'v0.2'

    redis_url: str = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    redis_key: str = os.getenv('REDIS_KEY', 'statping-health-check')

    db_name: str = os.getenv('DB_NAME', 'test_db')
    db_user: str = os.getenv('DB_USER', 'test_user')
    db_pass: str = os.getenv('DB_PASS', 'test_pass')
    db_host: str = os.getenv('DB_HOST', 'localhost')
    db_port: str = os.getenv('DB_PORT', '5432')
    db_conn: str = 'host={0} user={1} dbname={2} password={3}'.format(db_host, db_user, db_name, db_pass)
    db_check_sql: str = 'SELECT 1;'


settings = Settings()
