FROM debian:bullseye-slim

COPY ./entrypoint.sh /usr/local/bin/

RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y gettext nginx && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /etc/nginx/conf.d/* && \
    rm -rf /etc/nginx/sites-enabled/* && \
    rm -rf /etc/nginx/sites-available/* && \
    rm -rf /etc/nginx/nginx.conf && \
    rm -rf /var/www/html/* && \
    chmod +x /usr/local/bin/entrypoint.sh

COPY ./nginx.conf /etc/nginx/templates/nginx.conf.template

EXPOSE 80 443

CMD [ "/usr/local/bin/entrypoint.sh" ]
