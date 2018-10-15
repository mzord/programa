from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, length


class MyForm(FlaskForm):
    date = StringField('date', validators=[DataRequired(), length(min=4, max=4)])
    time = StringField('time', validators=[DataRequired()])
    