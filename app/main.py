from app import app
from app import db
from posts.blueprint import posts
from users.view import users

app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(users, url_prefix='/login')

if __name__ == '__main__':
    app.run()
