from app import app
from flask import redirect, render_template


@app.route('/')
@app.route('/index')
def index():
    return redirect('/news')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error/500.html'), 500
