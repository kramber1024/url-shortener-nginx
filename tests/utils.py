from collections.abc import Iterator
from pathlib import Path

from docker.models.containers import Container, ExecResult

NGINX_DIRECTORY: Path = Path(__file__).parent.parent / "nginx"
IMAGE_TAG: str = "nginx-test-image"
CONTAINER_NAME: str = "nginx-test"


def str_from_logs(logs: Iterator[dict[str, str]]) -> str:
    log_string: str = ""

    for log in logs:
        log_string += str(log[next(iter(log.keys()))])

    return log_string


def get_nginx_configuration(container: Container) -> str:
    result: ExecResult = container.exec_run("nginx -T")

    return str(result.output.decode("utf-8"))
