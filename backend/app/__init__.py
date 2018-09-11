from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_io import FlaskIO
#from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from werkzeug.utils import secure_filename


db = SQLAlchemy()
ma = Marshmallow()
io = FlaskIO()
#lm = LoginManager()
#lm.session_protection = 'strong'

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def create_app(config_name):
    from config import config
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['JWT_ACCESS_COOKIE_NAME'] = 'token'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    #app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    db.init_app(app)
    ma.init_app(app)
    io.init_app(app)
    #lm.init_app(app)
    jwt = JWTManager(app)



    from .api import api as api_blueprint
    #app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(api_blueprint)

    return app
