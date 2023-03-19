from typing import Generator

import pytest
from fastapi.testclient import TestClient
from app.db.session import TestSessionLocal, test_engine
from app.main import app
from app.db.base_class import Base


@pytest.fixture(scope="function", autouse=True)
def db() -> Generator:
    database = TestSessionLocal()
    database.begin()
    Base.metadata.create_all(test_engine, checkfirst=True)

    yield database

    database.flush()
    database.rollback()
    Base.metadata.drop_all(test_engine, checkfirst=True)
    database.close()



@pytest.fixture(scope="function")
def client() -> Generator:

    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides['get_db'] = _get_test_db
    with TestClient(app) as client:
        yield client
