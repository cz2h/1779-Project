from flask import Flask
from routes.file_routes import file_blueprint
from config import Config
from extensions import mysql

frontend_app = Flask(__name__)
frontend_app.debug = True

mysql.init_app(frontend_app)

frontend_app.register_blueprint(file_blueprint)

frontend_app.config.from_object(Config.DevConfig)
