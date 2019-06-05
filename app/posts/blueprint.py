import view, sys

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask_login import login_required

from models import Post, Tag
from .forms import PostForm, TagForm
from app import db


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('admin/')
@login_required
def admin_panel():
    post = Post.query.all()
    tags = Tag.query.all()

    return render_template('admin/admin_panel.html', posts=post, tags=tags)


@posts.route('/admin/posts/create', methods=['POST', 'GET'])
@login_required
def create_post():
    form = PostForm()

    if request.method == 'POST' and form.validate():
        title = form.title.data
        description = form.description.data
        tags = form.tags.data

        try:
            post = Post(title=title, description=description, tags=tags)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something wrong')

        return redirect(url_for('posts.index'))

    return render_template('admin/create_post.html', form=form)


@posts.route('/admin/posts/<slug>/update', methods=['POST', 'GET'])
@login_required
def update_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    form = PostForm(obj=post)

    if request.method == 'POST' and form.validate():
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    return render_template('admin/update_post.html', post=post, form=form)


@posts.route('admin/posts/<slug>/delete', methods=['POST', 'GET'])
@login_required
def delete_post(slug):
    post = Post.query.filter(Post.slug == slug).first()

    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()

        return redirect(url_for('posts.admin_panel'))

    return render_template('admin/delete_post.html', post=post)


@posts.route('admin/tags/create', methods=['POST', 'GET'])
@login_required
def create_tag():
    form = TagForm()

    if request.method == 'POST' and form.validate():
        name = form.name.data

        try:
            tag = Tag(name=name)
            db.session.add(tag)
            db.session.commit()
        except:
            print('Something wrong')

        return redirect(url_for('posts.admin_panel'))

    return render_template('admin/create_tag.html', form=form)


@posts.route('/admin/tags/<slug>/update', methods=['POST', 'GET'])
@login_required
def update_tag(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    form = TagForm(obj=tag)

    if request.method == 'POST' and form.validate():
        form = TagForm(formdata=request.form, obj=tag)
        form.populate_obj(tag)
        db.session.commit()

        return redirect(url_for('posts.admin_panel', slug=tag.slug))

    return render_template('admin/update_tag.html', tag=tag, form=form)


@posts.route('admin/tags/<slug>/delete', methods=['POST', 'GET'])
@login_required
def delete_tag(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()

    if request.method == 'POST':
        db.session.delete(tag)
        db.session.commit()

        return redirect(url_for('posts.admin_panel'))

    return render_template('admin/delete_tag.html', tag=tag)


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
