from flask import Blueprint, render_template, url_for, request, redirect
from jinja2 import Environment, FileSystemLoader
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
        print("Batch size entered",BatchSize)
        return redirect(url_for('views.gan', BatchSize= BatchSize))
    return render_template(home_template, url_for=url_for)

@views.route('/gan', methods=['GET'])
def gan():
    BatchSize = int(request.args.get('BatchSize'))  # Parse BatchSize as integer
    gan_model = load_model('C:/Users/jagmeet.singh/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/generator_healthy_cherry_BiGAN.h5')
    # gan_model = load_model('C:/Users/jagme/Documents/GitHub/WebApp_GAN/Webapp/GAN_saved_models/cherry/generator_mildew_cherry_BiGAN.h5')
    random_latent_vector = tf.random.normal(shape=(BatchSize, 100))
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
    return render_template(gan_template, url_for=url_for, flag=flag, gan_model=gan_model, BatchSize=BatchSize, generated_images=generated_images, image_files=image_files)



# import tensorflow as tf
# import keras
# random_latent_vectors = tf.random.normal(shape=(2000, 100))
# generated_images = bigan.generator.predict(random_latent_vectors)
# generated_images = generated_images * 255.0
# for i in range(len(generated_images)):
#     img = keras.preprocessing.image.array_to_img(generated_images[i])
#     img.save(os.path.join('BiGAN_strawberry_leafScorch_final/strawberry_leafScorch', f'generated_img_epoch_{i}.png'))