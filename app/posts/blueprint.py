import view

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for

from sqlalchemy import desc

from models import Post, Tag
from .forms import PostForm
from app import db


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        try:
            post = Post(title=title, description=description)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something wrong')
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/<slug>/update', methods=['POST', 'GET'])
def update_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/update_post.html', post=post, form=form)


@posts.route('/<slug>/delete', methods=['POST', 'GET'])
def delete_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    print('test')
    print(dir(post))
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('posts.index'))

    return render_template('posts/delete_post.html', post=post)


@posts.route('/')
def index():
    q = request.args.get('q')
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        post = Post.query.filter(Post.title.contains(q) | Post.description.contains(q))
    else:
        post = Post.query.order_by(Post.date_pub.desc())

    pages = post.paginate(page=page, per_page=5)
    return render_template('posts/index.html', pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags

    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()

    return render_template('posts/tag_detail.html', tag=tag, posts=posts)
