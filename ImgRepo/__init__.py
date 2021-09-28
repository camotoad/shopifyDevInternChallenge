from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ImgRepo.db'

    from ImgRepo.main.routes import main
    from ImgRepo.posts.routes import posts
    from ImgRepo.errors.handlers import errors

    db.init_app(app)
    app.config['SECRET_KEY'] = os.environ.get('SK_FlaskBlog')

    with app.app_context():
        db.create_all()
    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app


db = SQLAlchemy()
