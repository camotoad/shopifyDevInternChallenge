from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    picture = FileField('Upload a Picture', validators=[FileAllowed(['png', 'jpg', 'bmp'])])
    tags = StringField('Tags')
    submit = SubmitField('Post')

class UpdatePostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    picture = FileField('Upload a Picture', validators=[FileAllowed(['png', 'jpg', 'bmp'])])
    tags = StringField('Tags')
    submit = SubmitField('Update')
#
# class SearchForm(FlaskForm):
#     tags = StringField('Tags', validators=[DataRequired()])
#     submit = SubmitField('Search')