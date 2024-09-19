import uvicorn

from src.config.config import settings

if __name__ == "__main__":
    if settings.STAGE == "dev":
        uvicorn.run(
            "src.main:app",
            host=settings.HOST,
            port=settings.SERVICE_PORT,
            reload=True,
        )
    elif settings.STAGE == "prod":
        uvicorn.run(
            "src.main:app",
            host=settings.HOST,
            port=settings.SERVICE_PORT,
            workers=settings.WORKERS,
        )
