#!/bin/bash

if [ -z "$WEB_SERVER_HOST" ] || [ -z "$WEB_SERVER_PORT" ]; then
    export WEB_SERVER_HOST=localhost
    export WEB_SERVER_PORT=8000
fi

INPUT_TEMPLATE="/etc/nginx/templates/nginx.conf.template"
OUTPUT_FILE="/etc/nginx/nginx.conf"

envsubst '${WEB_SERVER_HOST},${WEB_SERVER_PORT}' < "$INPUT_TEMPLATE" > "$OUTPUT_FILE"
exec "$@"
