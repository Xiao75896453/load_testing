from abc import ABC
from dataclasses import dataclass

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


@dataclass
class DBUrlParameter:
    user: str
    password: str
    host: str
    port: int
    database: str


@dataclass
class DBConnectionParameter:
    pool_size: int
    max_overflow: int
    pool_recycle: int


DB_BASE = declarative_base()


class ORM(ABC):
    def __init__(
        self,
        db_driver: str,
        db_url_parameter: DBUrlParameter,
        db_connection_parameter: DBConnectionParameter,
    ) -> None:
        self.__db_driver: str = db_driver
        self.__db_url_parameter: DBUrlParameter = db_url_parameter
        self._db_url: str
        self._db_connection_parameter: DBConnectionParameter = db_connection_parameter

        self.__init_db_rul()

    def __init_db_rul(self) -> None:
        self._db_url = (
            rf"{self.__db_driver}://"
            + f"{self.__db_url_parameter.user}:{self.__db_url_parameter.password}"
            + f"@{self.__db_url_parameter.host}:{self.__db_url_parameter.port}/{self.__db_url_parameter.database}"
        )


class SqlAlchemySync(ORM):
    def __init__(
        self,
        db_driver: str,
        db_url_parameter: DBUrlParameter,
        db_connection_parameter: DBConnectionParameter,
    ) -> None:
        super().__init__(
            db_driver=db_driver,
            db_url_parameter=db_url_parameter,
            db_connection_parameter=db_connection_parameter,
        )
        self.__engine = create_engine(
            self._db_url,
            pool_size=self._db_connection_parameter.pool_size,
            max_overflow=self._db_connection_parameter.max_overflow,
            pool_recycle=self._db_connection_parameter.pool_recycle,
        )
        self.__session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.__engine
        )

    def get_db_session(self):
        with self.__session() as db_session:
            yield db_session


class SqlAlchemyAsync(ORM):
    def __init__(
        self,
        db_driver: str,
        db_url_parameter: DBUrlParameter,
        db_connection_parameter: DBConnectionParameter,
    ) -> None:
        super().__init__(
            db_driver=db_driver,
            db_url_parameter=db_url_parameter,
            db_connection_parameter=db_connection_parameter,
        )
        self.__engine = create_async_engine(
            self._db_url,
            pool_size=self._db_connection_parameter.pool_size,
            max_overflow=self._db_connection_parameter.max_overflow,
            pool_recycle=self._db_connection_parameter.pool_recycle,
        )
        self.__session = async_sessionmaker(
            autocommit=False, autoflush=False, bind=self.__engine
        )

    async def get_db_session(self):
        async with self.__session() as db_session:
            yield db_session
