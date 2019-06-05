#! /usr/bin/env python
from app import app
from app import db
from posts.blueprint import posts
from users.views import users

app.register_blueprint(users, url_prefix='/')
app.register_blueprint(posts, url_prefix='/blog')


if __name__ == '__main__':
    app.run()
