from wtforms import Form, StringField, TextAreaField    # выстраивают соответствие между моделями и html формами


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
