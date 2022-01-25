import os

from flask import Flask
from admin import admin
from news import news

app = Flask(__name__, static_folder="static")
app.secret_key = os.urandom(24)

app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(admin.admin)
app.register_blueprint(news.news)
from app import routes