# DEMO
> PyCon TW 2024 talk [Using Load Testing to Unveil Performance Differences Between Sync and Async: Web Server as a Case Study](https://tw.pycon.org/2024/zh-hant/conference/talk/317)

---
# Projects
## account_password_management
[![My Skills](https://skillicons.dev/icons?i=python,fastapi,postgresql&theme=light)](https://skillicons.dev)

- Load Testing Tool : [Locust](https://locust.io/)
- Backend Framework : [FastAPI](https://fastapi.tiangolo.com/) (async)
- ASGI Web Server : [Uvicorn](https://www.uvicorn.org/)
- Database : [PostgreSQL](https://www.postgresql.org/)
- ORM : [SQLAlchemy](https://www.sqlalchemy.org/)
- Load Balance : [Nginx](https://nginx.org/en/) 
- lint : [ruff](https://github.com/astral-sh/ruff)、[isort](https://pycqa.github.io/isort/index.html)

### Requirements
- python 3.11+
- poetry

### Installation
1. Clone the repo
    ```bash
    git clone
    ```
1. Install Python packages
    ```bash
    poetry install
    ```
1. Install PostgreSQL
1. Set PostgreSQL account
1. Create DB and Schema
2. Create `.env`

    `.env` example
    ```.env
    STAGE="prod"
    SERVICE_PORT=3000
    WORKERS=1
    HOST="0.0.0.0"

    DB_HOST="localhost"
    DB_PORT="5432"
    DB_USER="postgres"
    DB_PASSWORD="password"
    DB_DATABASE="load_testing"
    DB_POOL_SIZE=10
    DB_MAX_OVERFLOW=5
    DB_POOL_RECYCLE=300
    ```

### Usage
- Startup the services
    ```bash
    python app.py
    ```
- Execute load testing
    ```bash
    locust --config .\locust_files\demo_config.conf {User Class}
    ```

### API Document
1. Startup the services
2. Open a browser to http://localhost:3000/docs#

---
# Contact
TingYi Xiao - a75896453@gmail.com

---
# Acknowledgments
- [Locust](https://locust.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Poetry](https://python-poetry.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Nginx](https://nginx.org/en/) 
- [README](https://github.com/othneildrew/Best-README-Template)