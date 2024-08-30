#!/bin/bash

INPUT_TEMPLATE="/etc/nginx/templates/nginx.conf.template"
OUTPUT_FILE="/etc/nginx/nginx.conf"

# Replace placeholders in the template file with the values of the environment variables
envsubst '${API_SERVER_HOST},${API_SERVER_PORT},${WEB_SERVER_HOST},${WEB_SERVER_PORT}' < "$INPUT_TEMPLATE" > "$OUTPUT_FILE"

# Start Nginx
nginx -g "daemon off;"
