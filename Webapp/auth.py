from flask import Flask, Blueprint, url_for, render_template
from jinja2 import Environment, FileSystemLoader

auth = Blueprint('auth', __name__)



@auth.route('/login')
def login():
    # backend function for login
    pass

@auth.route('/logout')
def logout():
    # backend function for logout
    pass

@auth.route('/signup')
def signup():
    # backend function for sign up
    pass
