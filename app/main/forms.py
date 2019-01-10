from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, \
                    SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User


class SearchForm(FlaskForm):
    q = StringField('Search', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)



class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    genre = SelectMultipleField('Choose your channel genre', choices=(('Sport', \
                                'Sport'), ('News', 'News'), ('Game', 'Game'), \
                                ('Movie', 'Movie'), ('Livestyle', 'Livestyle')))
    twitter = TextAreaField('Enter a link to your twitter account')
    youtube = TextAreaField('Enter a link to your youtube account')
    git = TextAreaField('Enter a link to your git account')
    facebook = TextAreaField('Enter a link to your facebook account')
    vk = TextAreaField('Enter a link to your vk account')
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')



class PostForm(FlaskForm):
    headline = TextAreaField('Enter the title (briefly)', validators=[DataRequired(), \
                             Length(min=3, max=25)])
    post = TextAreaField('Main Text', validators=[DataRequired()])
    submit = SubmitField('Submit')

