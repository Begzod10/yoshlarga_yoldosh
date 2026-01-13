from flask import Blueprint, render_template
from backend.models.models import User

components = Blueprint('components', __name__)


@components.route('/about')
def about():
    return render_template('components/about/about.html')


@components.route('/brave')
def brave():
    return render_template('components/brave/brave.html')


@components.route('/control_self')
def control_self():
    return render_template('components/controlSelf/controlSelf.html')


@components.route('/goal')
def goal():
    return render_template('components/goal/goal.html')


@components.route('/independence')
def independence():
    return render_template("components/independence/independence.html")


@components.route('/initiative')
def initiative():
    return render_template("components/Initiative/Initiative.html")


@components.route('/level')
def level():
    return render_template("components/level/htrml.html")


@components.route('/login')
def login():
    return render_template("components/login/login.html")


@components.route('/prinsipic')
def prinsipic():
    return render_template("components/prinsipic/prinsipic.html")
