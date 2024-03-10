"""Initializes the Flask application."""
from app import create_app

app = create_app('settings.py')

if __name__ == '__main__':
    app.run(debug=True)
