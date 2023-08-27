from flask import Blueprint, render_template, url_for
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader('C:/Users/jagme/Documents/GitHub/WebApp_GAN/Webapp/template'))
home_template = template_env.get_template('home.html')

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template(home_template, url_for=url_for)