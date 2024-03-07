#!/bin/sh

# Only then, once that "blocking forever" has finished...
exec sh -c "gunicorn --bind 0.0.0.0:8000 'app:create_app()'"
