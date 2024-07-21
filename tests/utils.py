from collections.abc import Iterator
from pathlib import Path

NGINX_DIRECTORY: Path = Path(__file__).parent.parent / "nginx"


def str_from_logs(logs: Iterator[dict[str, str]]) -> str:
    log_string: str = ""

    for log in logs:
        log_string += str(log[next(iter(log.keys()))])

    return log_string
