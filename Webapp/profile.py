from flask import Flask, render_template, url_for, Blueprint
from jinja2 import Environment, FileSystemLoader

profile = Blueprint('profile', __name__)

@profile.route('/profile')
def profile():
    # logic to displaying profile history of the use of GANs will
    pass