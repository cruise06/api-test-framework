import os
import pytest
from src.core.http_client import APIClient
from src.services.user_service import UserService

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev")

@pytest.fixture(scope="session")
def env(pytestconfig):
    env_value = pytestconfig.getoption("--env")
    os.environ["ENV"] = env_value
    return env_value

@pytest.fixture(scope="session")
def api_client(env):
    client = APIClient()
    yield client
    client.close()

@pytest.fixture(scope="session")
def user_service(api_client):
    return UserService(client=api_client)
