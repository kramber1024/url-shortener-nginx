from docker import DockerClient

from tests.utils import IMAGE_TAG, NGINX_DIRECTORY, str_from_logs


def test_build(client: DockerClient) -> None:
    image, logs = client.images.build(
        path=str(NGINX_DIRECTORY),
        dockerfile="Dockerfile",
        rm=True,
        forcerm=True,
        tag=IMAGE_TAG,
    )
    image.remove(force=True)
    logs_str: str = str_from_logs(logs)

    assert "FROM debian:bullseye-slim" in logs_str
    assert "COPY ./launch.sh /usr/local/bin/launch.sh" in logs_str
    assert (
        "apt-get install --no-install-recommends "
        "--no-install-suggests -y gettext nginx"
    ) in logs_str
    assert "COPY ./nginx.conf /etc/nginx/templates/nginx.conf.template" in logs_str
    assert "EXPOSE 80 443" in logs_str
    assert (
        'CMD [ "/usr/local/bin/launch.sh", '
        '"nginx", "-g", "daemon off;" ]'
    ) in logs_str
    assert image
    assert image.attrs.get("Config").get("ExposedPorts").get("80/tcp") is not None
    assert image.attrs.get("Config").get("ExposedPorts").get("443/tcp") is not None
    assert image.attrs.get("Config").get("Cmd") == [
        "/usr/local/bin/launch.sh", "nginx", "-g", "daemon off;",
    ]
