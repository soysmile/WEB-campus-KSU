from app import db, models
from wtforms import form, fields, validators


class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(models.User).filter_by(login=self.login.data).first()


class RegistrationForm(form.Form):
    first_name = fields.StringField(validators=[validators.required()])
    last_name = fields.StringField(validators=[validators.required()])
    department = fields.StringField(validators=[validators.required()])
    group = fields.IntegerField(validators=[validators.required()])
    birthday = fields.DateField(validators=[validators.required()])
    speciality = fields.StringField(validators=[validators.required()])
    p_series = fields.StringField(validators=[validators.required()])
    p_number = fields.IntegerField(validators=[validators.required()])
    date_of_issue = fields.DateField(validators=[validators.required()])
    issue = fields.StringField(validators=[validators.required()])
    phone_number = fields.IntegerField(validators=[validators.required()])

