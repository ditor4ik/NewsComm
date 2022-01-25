from flask import Blueprint, render_template, session, redirect, request, url_for
from database.sql import DataBase
from hashlib import sha512
from database import access

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

def validation_auth():
    if 'email' in session:
        db = DataBase()
        result = db.is_except('admin_acc', f'`email`="{session["email"]}" AND `password`="{session["password"]}"')
        db.close()
        return result
    else:
        return False

##################################################__ОСНОВА__############################################################

@admin.route('')
def index():
    valid = validation_auth()
    return render_template('admin/index.html') if valid else redirect(url_for('admin.login'))

@admin.route('/login')
def login():
    return render_template('admin/login_admin.html')

@admin.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        email = request.form['email']
        password = sha512(request.form['password'].encode('UTF-8')).hexdigest()
        db = DataBase()
        result = db.is_except('admin_acc', f'`email`="{email}" AND `password`="{password}"')

        if result is True:
            session['email'] = email
            session['password'] = password
            fullname = db.select('admin_acc', ['fullname'], f'`email`="{email}" AND `password`="{password}"')[0]
            session['fullname'] = fullname[0]
            db.close()
            return redirect(url_for('admin.index'))
        else:
            db.close()
            return render_template('admin/login_admin.html')

    return render_template('admin/login_admin.html')

@admin.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('admin.login'))

@admin.context_processor
def utility_processor():
    def access():
        pass

##################################################__РОЛИ__##############################################################

@admin.route('/table/role')
def table_role():
    valid = validation_auth()
    if valid:
        db = DataBase()
        data = db.select('role', ['id', 'name'])
        db.close()
        return render_template('table/role/table_view.html', data=data)
    else:
        return redirect(url_for('admin.login'))

###########################################__СЛУЖЕБНЫЕ_АККАУНТЫ__#######################################################