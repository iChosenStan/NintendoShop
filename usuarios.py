from flask import render_template, request, flash, redirect
from models import Usuario
from database import db
from flask import Blueprint, url_for

bp_usuarios = Blueprint('usuarios', __name__, template_folder='templates')

@bp_usuarios.route('/')
@bp_usuarios.route('/recuperar')
def recuperar():
  usuarios = Usuario.query.all()
  return render_template('usuarios_recuperar.html', usuarios = usuarios)

@bp_usuarios.route('/criar', methods=['GET', 'POST'])
def criar():
  if request.method == 'GET':
    return render_template('usuarios_criar.html')

  if request.method == 'POST':
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    u = Usuario(nome, email, senha)
    db.session.add(u)
    db.session.commit()
    
    return redirect(url_for('.recuperar'))

@bp_usuarios.route('/apagar/<id>', methods=['GET', 'POST'])
def apagar(id):
  u = Usuario.query.get(id)
  
  if request.method == 'GET':
    return render_template('usuarios_apagar.html', usuario = u)

  if request.method=='POST':
    db.session.delete(u)  
    db.session.commit()

  return redirect(url_for('.recuperar'))
  