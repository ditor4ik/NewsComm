from flask import Blueprint, render_template

news = Blueprint('news', __name__, url_prefix='/news', template_folder='templates')

@news.route('')
def index():
    return render_template('news/index.html')