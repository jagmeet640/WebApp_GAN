from flask import Blueprint, render_template, url_for, request, redirect
from jinja2 import Environment, FileSystemLoader
from flask_login import login_required, current_user
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import os

# template_env = Environment(loader=FileSystemLoader('C:/Users/jagme/Documents/GitHub/WebApp_GAN/Webapp/template'))
template_env = Environment(loader=FileSystemLoader('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/template'))
home_template = template_env.get_template('home.html')
gan_template = template_env.get_template('gan.html')

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        BatchSize = request.form.get('BatchSize')
        selected_gan = request.form['GanType']
        selected_plant = request.form['plant']
        print('selected gan ', selected_gan)
        print("Batch size entered",BatchSize)
        print("selected plant", selected_plant)
        return redirect(url_for('views.gan', BatchSize= BatchSize, selected_gan=selected_gan, selected_plant=selected_plant))
    return render_template(home_template, url_for=url_for, user=current_user)

@views.route('/gan', methods=['GET'])
def gan():

    BatchSize = int(request.args.get('BatchSize'))  # Parse BatchSize as integer
    selected_gan = request.args.get('selected_gan') # get selected gan option
    selected_plant = request.args.get('selected_plant') # get the selected plant

    if selected_gan == 'DCGAN':
        # gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/generator_healthy_cherry_DCGAN.h5')
        gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/Healthy_' + selected_plant + '_' + selected_gan + '.h5')
        random_latent_vector = tf.random.normal(shape=(BatchSize, 128))
    elif selected_gan == 'LSGAN':
        # gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/generator_healthy_cherry_LSGAN.h5')
        gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/Healthy_' + selected_plant + '_' + selected_gan + '.h5')
        random_latent_vector = tf.random.normal(shape=(BatchSize, 128))
    elif selected_gan == 'WGAN':
        # gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/generator_healthy_cherry_WGAN.h5')
        gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/Healthy_' + selected_plant + '_' + selected_gan + '.h5')
        random_latent_vector = tf.random.normal(shape=(BatchSize, 128))
    elif selected_gan == 'BIGAN' :
        # gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/generator_healthy_cherry_BiGAN.h5')
        gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/Healthy_' + selected_plant + '_' + selected_gan + '.h5')
        random_latent_vector = tf.random.normal(shape=(BatchSize, 100))
    else:
        print("error! Gan type not valid")

    # gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/generator_healthy_cherry_BiGAN.h5')
    # # gan_model = load_model('C:/Users/jagme/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/generator_mildew_cherry_BiGAN.h5')


    generated_images = gan_model.predict(random_latent_vector)
    generated_images = generated_images * 255.0
    for i in range(len(generated_images)):
        img = keras.preprocessing.image.array_to_img(generated_images[i])
        # C:\Users\jagmeet.singh\Documents\GitHub\WebApp_GAN\Webapp\static\generated_imgs   
        img.save(f'C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/static/generated_imgs/generated_image_{i}.png')  # Save the image
        # img.save(f'C:/Users/jagme/Documents/GitHub/WebApp_GAN/Webapp/generated_imgs/generated_image_{i}.png')  # Save the image

   
    if gan_model is not None: 
       flag = True
    else:
        flag = False

    image_files = os.listdir('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/static/generated_imgs')
    return render_template(gan_template, url_for=url_for, flag=flag, gan_model=gan_model, BatchSize=BatchSize, generated_images=generated_images, image_files=image_files, user=current_user)

    # print(selected_gan)
    # print(BatchSize)
    # return "<h1>worked</h1>"



# import tensorflow as tf
# import keras
# random_latent_vectors = tf.random.normal(shape=(2000, 100))
# generated_images = bigan.generator.predict(random_latent_vectors)
# generated_images = generated_images * 255.0
# for i in range(len(generated_images)):
#     img = keras.preprocessing.image.array_to_img(generated_images[i])
#     img.save(os.path.join('BiGAN_strawberry_leafScorch_final/strawberry_leafScorch', f'generated_img_epoch_{i}.png'))