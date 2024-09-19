from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.io_bound import query
from src.config.db import ASYNC_ORM, SYNC_ORM

router = APIRouter()


@router.post("/sync")
def sync_create_test_data(
    db_session: Session = Depends(SYNC_ORM.get_db_session),
):
    query.sync_create_test_data(db_session=db_session)


@router.get("/sync")
def sync_get_test_data(db_session: Session = Depends(SYNC_ORM.get_db_session)):
    test_data = query.sync_get_test_data(db_session=db_session)

    return test_data


@router.get("/sync/hello_world")
def sync_hello_world():

    return "hello world"


@router.patch("/sync")
def sync_update_test_data(
    db_session: Session = Depends(SYNC_ORM.get_db_session),
):
    query.sync_update_test_data(db_session=db_session)


@router.post("/async")
async def async_create_test_data(
    db_session: Session = Depends(ASYNC_ORM.get_db_session),
):
    await query.async_create_test_data(db_session=db_session)


@router.post("/async/but_sync_db_session")
async def async_create_test_data_but_sync_db_session(
    db_session: Session = Depends(SYNC_ORM.get_db_session),
):
    await query.async_create_test_data_but_sync_db_session(db_session=db_session)


@router.get("/async")
async def async_get_test_data(db_session: Session = Depends(ASYNC_ORM.get_db_session)):
    test_data = await query.async_get_test_data(db_session=db_session)

    return test_data


@router.get("/async/hello_world")
async def async_hello_world():

    return "hello world"


@router.patch("/async")
async def async_update_test_data(
    db_session: Session = Depends(ASYNC_ORM.get_db_session),
):
    await query.async_update_test_data(db_session=db_session)
