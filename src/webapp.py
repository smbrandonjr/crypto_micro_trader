from flask import Flask, render_template
from common.database.database import Database
from models.settings.view import setting_blueprint
import os

__author__ = 'mike.brandon|smbrandonjr@gmail.com'

webapp = Flask(__name__)
webapp.secret_key = os.environ.get("APP_KEY")
webapp.register_blueprint(setting_blueprint, url_prefix='/settings')


@webapp.before_first_request
def init_db():
    Database.initialize()


@webapp.route('/', methods=["GET", "POST"])
def index():
    return render_template('base.html')


if __name__ == "__main__":
    webapp.run(debug=True)