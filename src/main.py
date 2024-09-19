from fastapi import FastAPI

from src.api import cpu_bound, io_bound

API_PREFIX = "api"
IO_BOUND_API_ROUTE = f"/{API_PREFIX}/io_bound"
CPU_BOUND_API_ROUTE = f"/{API_PREFIX}/cpu_bound"

app = FastAPI()

app.include_router(
    io_bound.routers.router,
    prefix=IO_BOUND_API_ROUTE,
    tags=["I/O Bound"],
)

app.include_router(
    cpu_bound.routers.router,
    prefix=CPU_BOUND_API_ROUTE,
    tags=["CPU Bound"],
)
