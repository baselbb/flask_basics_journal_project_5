from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired


class EntryForm(FlaskForm):
    """Entry form to create a new blog entry"""
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    spent = StringField('Time Spent', validators=[DataRequired()])
    learned = StringField('What I learned', validators=[DataRequired()])
    resources = StringField('Resources to Remember', validators=[DataRequired()])
