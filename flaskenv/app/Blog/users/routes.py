from flask import Blueprint,render_template

users=Blueprint('users',__name__)



@users.route('/')
def index():
    user={'username':'sarpong'}
    return render_template('index.html',user=user)

@users.route('/profile/')
def profile():
    return render_template('profile.html')
