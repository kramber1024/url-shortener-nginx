# URL Shortener NGINX

<a href="https://github.com/kramber1024/url-shortener-nginx/actions/workflows/tests.yml" target="_blank"><img src="https://github.com/kramber1024/url-shortener-nginx/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>

## Features

- 🐋 [**Docker**](https://www.docker.com/) for production.
- ✅ Tests with [**Pytest**](https://pytest.org/).

> [!WARNING]
> This repository is part of a larger project that consists of multiple repositories. Using this repository on its own is not recommended, as it may not function correctly without the other components of the project. For complete functionality and proper integration, please refer to the [kramber1024/url-shortener](https://github.com/kramber1024/url-shortener).

## Usage

### Requirements

- 🐋 [**Docker**](https://www.docker.com/)

Please ensure that Docker is properly configured and *running* on your system.

### Installation

Clone repository:
```bash
git clone https://github.com/kramber1024/url-shortener-nginx.git
```

Change directory:
```bash
cd url-shortener-nginx
```

### Building an image from Dockerfile

Build the image using the following command:
```bash
docker build ./nginx -t nginx:latest
```

### Running the container

Run the container using the following command:
```bash
docker run -d -p 80:80 -p 443:443 --env WEB_SERVER_HOST=host.docker.internal --env WEB_SERVER_PORT=26802 --name container-name nginx
```
Arguments:
- `-p 80:80 -p 443:443` - Expose ports 80 and 443 to the host.
- `--env WEB_SERVER_HOST=host.docker.internal` - The host of the web server. You can replace `host.docker.internal` with the IP address of the web server.
- `--env WEB_SERVER_PORT=26802` - The port of the web server. You can replace `26802` with the port of the web server.
- `--name container-name` - The name of the container. You can replace `container-name` with any name you want.

### Running the container with Docker Compose

Run the container using the following command:
```bash
docker-compose up -d
```

To rebuild the container, use the following command:
```bash
docker-compose up -d --build
```

Edit the [**compose.yaml**](./compose.yaml) file to change launch configuration.

```yaml
name: docker-compose

services:
  nginx:
    container_name: nginx # Change the container name

    build:
      tags:
        - nginx:latest
      context: ./nginx
      dockerfile: Dockerfile

    ports: # Change the ports
      - "80:80"
      - "443:443"

    environment: # Change the environment variables
      - WEB_SERVER_HOST=host.docker.internal
      - WEB_SERVER_PORT=26802
```

## Running tests

### Requirements

- 🐋 [**Docker**](https://www.docker.com/)
- 🐍 [**Python 3.12**](https://www.python.org/)

### Installation

Clone repository:
```bash
git clone https://github.com/kramber1024/url-shortener-nginx.git
```

Change directory:
```bash
cd url-shortener-nginx
```

### Preparing the environment

Create a virtual environment:
```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:

    ```bat
    .\venv\Scripts\activate
    ```
- On Linux and macOS:

    ```bash
    source venv/bin/activate
    ```

Install Poetry:
```bash
pip install poetry
```

Install dependencies:
```bash
poetry install --only main --no-root
```

### Running the tests

Run the tests using the following command:
```bash
pytest
```
⚠️ **Make sure that Docker is running before running the tests.**

```bash
======================== test session starts ========================
platform win32 -- Python 3.12.2, pytest-8.2.2, pluggy-1.5.0
rootdir: C:\Users\UserName\url-shortener-nginx
configfile: pyproject.toml
collected 2 items

tests\test_build.py .                                          [ 50%]
tests\test_run.py .                                            [100%]

=================== 2 passed in 66.27s (0:01:06) ====================
```

## License

This project is licensed under the terms of the [**MIT license**](./LICENSE).
