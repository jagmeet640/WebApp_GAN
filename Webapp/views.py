from flask import Blueprint, render_template
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader('C:/Users/jagme/Documents/GitHub/WebApp_GAN/Webapp/template'))
base_home_page_template = template_env.get_template('base_home_page.html')

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template(base_home_page_template)