from sqlalchemy import Column, Integer, String

from src.utils.db_connector import DB_BASE


class TestData(DB_BASE):
    __tablename__ = "test_data"

    id = Column(Integer, primary_key=True)
    test_data = Column(String(32))
