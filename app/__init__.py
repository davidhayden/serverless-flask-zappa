from config import Config
from flask import Flask


app = Flask(__name__)

app.config.from_object(Config)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.main import bp as main_bp
app.register_blueprint(main_bp)
