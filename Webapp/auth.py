from flask import Flask, Blueprint, url_for, render_template, request
from jinja2 import Environment, FileSystemLoader
from .model import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

template_env = Environment(loader=FileSystemLoader('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/template'))
login_template = template_env.get_template("login.html")
signup_template = template_env.get_template("signup.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # backend function for login
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email) .first()
        if user:
            if check_password_hash(user.password, password):
                print("correct password")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
        else: 
            print("incorrect password")
    else:
        print("email does not exsist")
        redirect(url_for('auth.signup'))

    return render_template(login_template, url_for=url_for)

@auth.route('/logout')
def logout():
    # backend function for logout
    pass

@auth.route('/signup')
def signup():
    # backend function for sign up
    if request.method == 'POST':
        email = request.form.get('email')
        FirstName = request.form.get('first-name')
        password1 = request.form.get('password')
        password2 = request.form.get('password-check')

        user = User.query.filter_by(email=email).first()

        if user:
            print("user exsists")
        elif len(email) < 4:
            print("invalid email")
        elif len(FirstName) < 3: 
            print("invalid first name")
        elif password1 != password2:
            print("passwords not same")
        else: 
            new_user = User(email=email, FirstName=FirstName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            print("account created")
            return redirect(url_for('views.home'))
    return render_template(signup_template, url_for=url_for)
