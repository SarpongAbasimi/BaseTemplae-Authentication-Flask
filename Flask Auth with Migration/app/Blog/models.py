from Blog import db
from flask import app
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60),nullable=False,unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(140),nullable=False,unique=True)
    password = db.Column(db.String(60), nullable=False)
    location=db.Column(db.String(64))
    about_me=db.Column(db.Text())

    def __repr__(self):
        return 'User(%s,%s,%s)' %(self.name,self.email,self.password)
