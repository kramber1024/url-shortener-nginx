import docker
import pytest
from docker import DockerClient


@pytest.fixture(scope="session")
def client() -> DockerClient:
    client: DockerClient = docker.from_env()

    return client
