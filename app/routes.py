# app/routes.py
from flask import render_template, session, redirect, url_for, flash, request
from . import db
from .models import db, Disciplina
from flask import Blueprint
from datetime import datetime, timedelta, timezone

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    # Definindo o fuso horário de Brasília (UTC-3)
    brasilia_offset = timezone(timedelta(hours=-3))
    current_time = datetime.now(brasilia_offset)
    formatted_time = current_time.strftime('%B %d, %Y %I:%M %p')
    return render_template('index.html', current_time=formatted_time)

@main.route('/disciplinas', methods=['GET', 'POST'])
def disciplinas():
    if request.method == 'POST':
        name = request.form.get('name')
        semester = request.form.get('semester')

        nova_disciplina = Disciplina(name=name, semester=semester)
        db.session.add(nova_disciplina)
        db.session.commit()

        return redirect(url_for('main.disciplinas'))

    disciplinas = Disciplina.query.all()
    return render_template('disciplinas.html', disciplinas=disciplinas)

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
