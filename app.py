from flask import Flask
from routes.file_routes import file_blueprint
from routes.memcache_routes import memcache_blueprint

from config import Config
from extensions import mysql

from flask_cors import CORS

frontend_app = Flask(__name__)
CORS(frontend_app)

frontend_app.debug = True

mysql.init_app(frontend_app)

frontend_app.register_blueprint(file_blueprint)
frontend_app.register_blueprint(memcache_blueprint)

frontend_app.config.from_object(Config.DevConfig)

if __name__ == '__main__':
    frontend_app.run(host='127.0.0.1', port=114)
