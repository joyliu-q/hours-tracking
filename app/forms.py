from flask_wtf import FlaskForm
from wtforms import StringField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class InsertHours(FlaskForm):
    admin_first_name = StringField('Your First Name', validators=[DataRequired()])
    admin_last_name = StringField('Your Last Name', validators=[DataRequired()])
    project_title = StringField('Project Title', validators=[DataRequired()])
    project_date = DateField('Project Date', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Submit')
    