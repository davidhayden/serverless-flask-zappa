from flask import flash, redirect, render_template
from app.auth import bp
from app.auth.forms import LoginForm


@bp.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect("/index")

    return render_template('auth/login.html', form=form)
