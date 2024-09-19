from src.config.config import settings
from src.utils.db_connector import (DBConnectionParameter, DBUrlParameter,
                                    SqlAlchemyAsync, SqlAlchemySync)

POSTGRESQL_SYNC_DRIVER_NAME = "postgresql+psycopg2"
POSTGRESQL_ASYNC_DRIVER_NAME = "postgresql+asyncpg"

POSTGRESQL_URL_PARAMETER = DBUrlParameter(
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_DATABASE,
)

DB_CONNECTION_PARAMETER = DBConnectionParameter(
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    pool_recycle=settings.DB_POOL_RECYCLE,
)

SYNC_ORM = SqlAlchemySync(
    db_driver=POSTGRESQL_SYNC_DRIVER_NAME,
    db_url_parameter=POSTGRESQL_URL_PARAMETER,
    db_connection_parameter=DB_CONNECTION_PARAMETER,
)

ASYNC_ORM = SqlAlchemyAsync(
    db_driver=POSTGRESQL_ASYNC_DRIVER_NAME,
    db_url_parameter=POSTGRESQL_URL_PARAMETER,
    db_connection_parameter=DB_CONNECTION_PARAMETER,
)
