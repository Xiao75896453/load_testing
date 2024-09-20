from typing import List

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.models.test_data import TestData


def sync_create_test_data(db_session: Session) -> None:
    db_session.execute(insert(TestData).values({"test_data": "create"}))
    db_session.commit()


def sync_get_test_data(db_session: Session) -> List[TestData]:
    return db_session.scalars(select(TestData)).all()


def sync_update_test_data(db_session: Session) -> None:
    db_session.execute(
        update(TestData).where(TestData.id == 1).values({"test_data": "update"})
    )
    db_session.commit()


async def async_create_test_data(db_session: AsyncSession) -> None:
    await db_session.execute(insert(TestData).values({"test_data": "create"}))
    await db_session.commit()


async def async_create_test_data_but_sync_db_session(db_session: Session) -> None:
    db_session.execute(insert(TestData).values({"test_data": "create"}))
    db_session.commit()


async def async_get_test_data(db_session: AsyncSession) -> List[TestData]:
    return (await db_session.scalars(select(TestData))).all()


async def async_update_test_data(db_session: AsyncSession) -> None:
    await db_session.execute(
        update(TestData).where(TestData.id == 1).values({"test_data": "update"})
    )
    await db_session.commit()
