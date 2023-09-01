from flask import Flask, Blueprint, url_for, render_template
from jinja2 import Environment, FileSystemLoader

auth = Blueprint('auth', __name__)

template_env = Environment(loader=FileSystemLoader('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/template'))
login_template = template_env.get_template("login.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # backend function for login
    return render_template(login_template, url_for=url_for)

@auth.route('/logout')
def logout():
    # backend function for logout
    pass

@auth.route('/signup')
def signup():
    # backend function for sign up
    pass
