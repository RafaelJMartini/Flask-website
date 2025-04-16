from comunidadeimpressionadora import app,database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuario
from flask import render_template, redirect, url_for,flash,request


lista_usuarios = ['Rafael','João','Martini','Ronaldo']


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

        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        user = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(user)
        database.session.commit()
        flash(f"Conta criada com sucesso no e-mail {form_criarconta.email.data}", 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html',form_login = form_login,form_criarconta = form_criarconta)
