from collections.abc import Generator
from typing import TYPE_CHECKING

import docker
import pytest
from docker import DockerClient
from docker.models.images import Image

from tests.utils import CONTAINER_NAME, IMAGE_TAG, NGINX_DIRECTORY

if TYPE_CHECKING:
    from docker.models.containers import Container


@pytest.fixture(scope="session")
def client() -> DockerClient:
    client: DockerClient = docker.from_env()

    return client


@pytest.fixture
def image(client: DockerClient) -> Generator[Image, None, None]:
    image, _ = client.images.build(
        path=str(NGINX_DIRECTORY),
        dockerfile="Dockerfile",
        rm=True,
        forcerm=True,
        tag=IMAGE_TAG,
    )

    yield image

    try:
        container: Container = client.containers.get(CONTAINER_NAME)
        container.stop()
        container.remove(force=True)
    except docker.errors.NotFound:
        pass

    image.remove(force=True)
