from flask import Flask, render_template, request, flash, redirect,url_for
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

lista_usuarios = ['Rafael','João','Martini','Ronaldo']

app.config['SECRET_KEY'] = os.getenv('KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'


database = SQLAlchemy(app)      # Cria um banco de dados


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)

@app.route('/login', methods=["GET","POST"])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        #Fez login com sucesso
        flash(f'Login feito com sucesso no e-mail {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
        #enviar msg e redirecionar
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        #Criou a conta
        flash(f"Conta criada com sucesso no e-mail {form_criarconta.email.data}", 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html',form_login = form_login,form_criarconta = form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)