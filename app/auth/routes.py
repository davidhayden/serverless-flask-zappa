from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user
from app.auth import bp
from app.auth.forms import LoginForm
from app.models import load_user, login_valid


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        if not login_valid(form.username.data, form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('auth.login'))
        
        user = load_user(1)
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('main.index')

        return redirect(next_page)

    return render_template('auth/login.html', form=form)

@bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))
