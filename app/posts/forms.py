from wtforms import Form, StringField, TextAreaField


class PostForm(Form):
    title = StringField('Title')
    description = TextAreaField('Description')
