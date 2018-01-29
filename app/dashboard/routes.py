from flask import render_template
from flask_login import login_required
from app.dashboard import bp


@bp.route('/dashboard', methods=['GET'])
@login_required
def index():
    return render_template('dashboard/index.html')
