from app import create_app
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(dir_path, 'config.py')
app = create_app(config_path)

if __name__ == '__main__':
  app.run(debug=True)
