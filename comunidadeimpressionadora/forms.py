from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField,SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired,Email,Length, EqualTo,ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user

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

class FormEditarPerfil(FlaskForm):
     username  = StringField('Username',validators=[DataRequired()])
     email = StringField('E-mail', validators=[DataRequired(), Email()])
     foto_perfil = FileField('Atualizar foto de perfil', validators=[FileAllowed(['jpg','png'])])

     curso_excel = BooleanField('Curso excel')
     curso_vba = BooleanField('Curso VBA')
     curso_powerbi = BooleanField('Curso Powerbi')
     curso_python = BooleanField('Curso Python')
     curso_ppt = BooleanField('Curso Powerpoint')
     curso_sql = BooleanField('Curso SQL')

     botao_submit_editar_perfil = SubmitField('Confirmar Edição')

     def validate_email(self,email):
          print('a')
          if current_user.email != email.data:
               print('b')
               usuario = Usuario.query.filter_by(email=email.data).first()
               if usuario:
                    print('c')
                    raise ValidationError('Já existe um usuário com esse E-mail!')



class FormCriarPost(FlaskForm):
     titulo = StringField('Título do post',validators=[DataRequired(),Length(2,140)])
     corpo = TextAreaField('Escreva seu post aqui',validators=[DataRequired()])
     botao_submit = SubmitField('Criar Post')