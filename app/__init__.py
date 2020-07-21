from config import Config

from flask import Flask, escape, request, url_for, render_template, make_response, g, session
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Applying the config
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes


# from app import routes, models