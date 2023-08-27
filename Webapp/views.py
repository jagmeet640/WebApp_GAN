from flask import Blueprint, render_template, url_for, request, redirect
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader('C:/Users/jagme/Documents/GitHub/WebApp_GAN/Webapp/template'))
home_template = template_env.get_template('home.html')

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        BatchSize = request.form.get('BatchSize')
        print("Batch size entered",BatchSize)
        return redirect(url_for('views.gan', BatchSize= BatchSize))
    return render_template(home_template, url_for=url_for)

@views.route('/gan', methods=['GET'])
def gan():
    BatchSize = request.args.get('BatchSize')
    print("batch size from /gan :", BatchSize)
    return "<h1>GAN</h1>"