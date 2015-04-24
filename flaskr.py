from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
#from metamind.api import set_api_key#, classificationData, classificationModel
import os
import random

#set_api_key("k3U0ZYw5U7BiQWnXYCAJGzKHmSk42VSNUoVebKxPC9jlchnXzk")
app =Flask('tumor_classification')





def get_random_image():
	images = os.listdir('static/images/jpg')
	return random.choice(images)

@app.route('/')
def show_entries():
	image_filepath = "static/images/jpg/"+ get_random_image()
	return render_template('index.html',image_filepath=image_filepath)

@app.route('/tumor')
def shasdfasdf():
	image_filepath = "static/images/jpg/"+ get_random_image()
	return render_template('index.html',image_filepath=image_filepath)

@app.route('/not_tumor')
def asjdfhohrewjg():
	image_filepath = "static/images/jpg/"+ get_random_image()
	return render_template('index.html',image_filepath=image_filepath)

#with app.


####### 
#######
#######
#######
#######


if __name__ == '__main__':
	app.run() 
