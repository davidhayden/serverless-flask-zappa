from config import Config
from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'auth.login'

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.main import bp as main_bp
app.register_blueprint(main_bp)
