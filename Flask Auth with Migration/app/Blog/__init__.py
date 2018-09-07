from flask import Flask,url_for,render_template
from Blog.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
import os

app=Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate=Migrate(app,db)

manager=Manager(app)
manager.add_command('db',MigrateCommand)

bcrypt=Bcrypt(app)

from Blog.users.routes import users
from Blog.auth.routes import auth

app.register_blueprint(users)
app.register_blueprint(auth)
