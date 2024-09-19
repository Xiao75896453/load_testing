from fastapi import APIRouter

router = APIRouter()

CPU_BOUND_RUN_TIMES = 1000000


@router.get("/sync")
def sync_cpu_bound():
    for _ in range(CPU_BOUND_RUN_TIMES):
        pass


@router.get("/async")
async def async_cpu_bound():
    for _ in range(CPU_BOUND_RUN_TIMES):
        pass
