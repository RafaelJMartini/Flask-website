from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField
from wtforms.validators import DataRequired,Email,Length, EqualTo,ValidationError
from comunidadeimpressionadora.models import Usuario

class FormCriarConta(FlaskForm):

     username = StringField('Nome de Usuário',validators=[DataRequired()])
     email = StringField('E-mail',validators=[DataRequired(),Email()])
     senha = PasswordField('Senha',validators=[DataRequired(),Length(6,20)])
     confirmacao_senha = PasswordField('Confirmação da Senha',validators=[DataRequired(),EqualTo('senha')])
     botao_submit_criarconta = SubmitField('Criar Conta')


     def validate_email(self,email):
          usuario = Usuario.query.filter_by(email=email.data).first()
          if usuario:
               raise ValidationError('E-mail já cadastrado.')


class FormLogin(FlaskForm):
     email = StringField('E-mail',validators=[DataRequired(),Email()])
     senha = PasswordField('Senha',validators=[DataRequired(),Length(6,20)])
     lembrar_dados = BooleanField('Lembrar dados de acesso')
     botao_submit_login = SubmitField('Fazer Login')

