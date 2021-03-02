import alembic
import pytest
from alembic.config import Config
from sqlalchemy.orm import Session

from starlette.testclient import TestClient

from database.postgresql import Base, engine, SessionLocal
from main import app


@pytest.fixture(scope='session')
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(scope='function')
def db() -> Session:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session")
def apply_migrations() -> None:
    config = Config("alembic.ini")
    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")
