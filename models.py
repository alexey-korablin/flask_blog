from app import db  # экземпляр класса SQLAlchemy
from datetime import datetime
from re import sub


def slugify(s):
    pattern = r'[^\w+]'
    return sub(pattern, '-', s)


post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                     )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic')) # lazy='dynamic' -
    # данный параметр говорит, что при обращении к соответствующему свойству мы получаем объект base query (итерируемый
    # объект)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '{}'.format(self.name)  # определяет то, как будет выглядеть вывод объекта
        # в текстовом виде. Например запись '<Tag id: {}, name: {}>'.format(self.id, self.name) выведет: Tag id: 1,
        # name: flask ; если self.id = 1, self.name = flask

