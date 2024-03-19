#!/bin/sh

echo "Printing all environment variables:"

exec sh -c "gunicorn --bind 0.0.0.0:8000 'app:create_app()'"
