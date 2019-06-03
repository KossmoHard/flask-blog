from wtforms import Form, StringField, TextAreaField, SelectMultipleField


class PostForm(Form):
    title = StringField('Title')
    description = TextAreaField('Description')