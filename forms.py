from wtforms.fields import SelectField, StringField, PasswordField, SubmitField, FileField
from flask_wtf import FlaskForm


class SelectGroupForm(FlaskForm):
    grChoices = []
    group = SelectField('group', choices=grChoices)
    dayChoice = []
    day = SelectField('day', choices=dayChoice)
    submit = SubmitField('Показать')


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Submit')


class addPrepForm(FlaskForm):
    fioField = StringField('Фамилия Имя Отчество')
    dolgnostField = StringField('Должность')
    stepenChoices = ['нет', 'к.т.н', 'д.т.н']
    stepenField = SelectField('Науч. степень', choices=stepenChoices)
    photoField = FileField()
    submit = SubmitField('Добавить')


class addPrepForm(FlaskForm):
    fioField = StringField('Фамилия Имя Отчество')
    dolgnostField = StringField('Должность')
    grChoices = []
    group = SelectField('group', choices=grChoices)
    dayChoice = []
    day = SelectField('day', choices=dayChoice)
    stepenChoices = ['нет', 'к.т.н', 'д.т.н']
    stepenField = SelectField('Науч. степень', choices=stepenChoices)
    photoField = FileField()
    submit1 = SubmitField('Показать')

