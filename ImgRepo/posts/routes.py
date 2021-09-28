import os
import secrets

from flask import Blueprint, url_for, render_template, redirect, request, flash, current_app

from ImgRepo import db
from ImgRepo.models import Post
from ImgRepo.posts.forms import NewPostForm, UpdatePostForm

posts = Blueprint('posts', __name__)

def save_picture(picture):
    random = secrets.token_hex(10)
    _, extension = os.path.splitext(picture.filename)
    file_name = random + extension
    picture_path = os.path.join(current_app.root_path, 'static/pics', file_name)
    picture.save(picture_path)

    return file_name

@posts.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        if form.picture.data:
            print('here')
            picture_file = save_picture(form.picture.data)
            post = Post(title=form.title.data, image_file=picture_file, tags=form.tags.data)
            db.session.add(post)
            db.session.commit()
            flash('Post created', 'success')
            return redirect(url_for('main.home'))
    return render_template('new_post.html', title='Create a new post', form=form, legend='Create a new post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = UpdatePostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        picture_file = save_picture(form.picture.data)
        post.image_file = picture_file
        db.session.commit()
        flash('Post has been updated.', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.picture.data = post.image_file
    return render_template('new_post.html', title='Update post', form=form, legend='Update Post')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.route("/search/")
def search():
    tags = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    post = Post.query.filter(Post.tags.like(f'%{tags}%') | Post.title.like(f'%{tags}%')) \
        .order_by(Post.date_posted.desc()) \
        .paginate(page=page, per_page=5)
    print(post)
    return render_template('search.html', search=tags, posts=post)