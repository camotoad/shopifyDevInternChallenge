from flask import Blueprint
from flask import render_template, request
from ImgRepo.models import Post
# from ImgRepo.posts.forms import SearchForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    # form = SearchForm()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=8)
    return render_template('home.html', posts=posts)