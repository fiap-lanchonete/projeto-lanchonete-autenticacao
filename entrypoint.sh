#!/bin/sh

exec sh -c "gunicorn --bind 0.0.0.0:8000 'app:create_app()'"
