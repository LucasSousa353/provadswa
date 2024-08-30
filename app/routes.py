# app/routes.py
from flask import render_template, session, redirect, url_for, flash, request
from . import db
from .models import User, Role
from .forms import NameForm
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/disciplinas')
def disciplinas():
    roles = Role.query.all()
    return render_template('disciplinas.html')


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
