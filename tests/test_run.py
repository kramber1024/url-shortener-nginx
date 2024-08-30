import http
from typing import Any

import requests
from docker import DockerClient
from docker.models.containers import Container
from docker.models.images import Image

from tests.utils import CONTAINER_NAME, get_nginx_configuration


def test_run(client: DockerClient, image: Image) -> None:
    api_server_host: str = "127.0.0.1"
    api_server_port: str = "26801"
    web_server_host: str = "127.0.0.1"
    web_server_port: str = "26803"

    container: Container = client.containers.run(
        image,
        name=CONTAINER_NAME,
        ports={
            "80/tcp": "80",
            "443/tcp": "443",
        },
        environment={
            "WEB_SERVER_HOST": web_server_host,
            "WEB_SERVER_PORT": web_server_port,
            "API_SERVER_HOST": api_server_host,
            "API_SERVER_PORT": api_server_port,
        },
        detach=True,
    )

    assert isinstance(container, Container)

    nginx_configuration: str = get_nginx_configuration(container)
    assert "syntax is ok" in nginx_configuration
    assert "test is successful" in nginx_configuration
    assert "server_name nginx;" in nginx_configuration
    assert "server_tokens off;" in nginx_configuration
    assert f"{api_server_host}:{api_server_port}" in nginx_configuration
    assert f"{web_server_host}:{web_server_port}" in nginx_configuration
    assert "${" not in nginx_configuration

    attrs: dict[str, Any] = container.attrs
    assert attrs.get("Path") == "/usr/local/bin/entrypoint.sh"
    assert attrs.get("Args") == []
    assert attrs.get("Platform") == "linux"
    assert (
        attrs.get("HostConfig", {})
        .get(
            "PortBindings",
        )
        .get("443/tcp")[0]
        .get("HostPort")
        == "443"
    )
    assert (
        attrs.get("HostConfig", {})
        .get(
            "PortBindings",
        )
        .get("80/tcp")[0]
        .get("HostPort")
        == "80"
    )
    assert f"API_SERVER_HOST={api_server_host}" in attrs.get("Config", {}).get("Env")
    assert f"API_SERVER_PORT={api_server_port}" in attrs.get("Config", {}).get("Env")
    assert f"WEB_SERVER_HOST={web_server_host}" in attrs.get("Config", {}).get("Env")
    assert f"WEB_SERVER_PORT={web_server_port}" in attrs.get("Config", {}).get("Env")

    response: requests.Response = requests.get("http://localhost", timeout=5)
    assert response.status_code == http.HTTPStatus.BAD_GATEWAY
    assert response.headers.get("Server") == "nginx"
    assert response.headers.get("Content-Type") == "text/html"
