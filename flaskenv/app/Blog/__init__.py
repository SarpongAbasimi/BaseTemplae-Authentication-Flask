from flask import Flask,url_for,render_template
from Blog.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

app=Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)

from Blog.users.routes import users
from Blog.auth.routes import auth

app.register_blueprint(users)
app.register_blueprint(auth)
