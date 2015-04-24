from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
#from metamind.api import set_api_key#, classificationData, classificationModel
import os
import random
import json
#set_api_key("k3U0ZYw5U7BiQWnXYCAJGzKHmSk42VSNUoVebKxPC9jlchnXzk")
app =Flask('tumor_classification')

####### 
#######
#######
#######
####### TCIAClient setup.... 

from tciaclient import TCIAClient
import urllib2, urllib,sys
####################################  Function to print server response #######
def printServerResponse(response):
    if response.getcode() == 200:
        print "Server Returned:\n"
        print response.read()
        print "\n"
    else:
        print "Error: " + str(response.getcode())

####################################  Create Clients for Two Different Resources  ####
tcia_client = TCIAClient(apiKey = "api_key_here",baseUrl="https://services.cancerimagingarchive.net/services/v2",resource = "TCIA")
tcia_client2 = TCIAClient(apiKey ="api_key_here",baseUrl="https://services.cancerimagingarchive.net/services/v2",resource="SharedList")


#######
#######
#######
#######
#######



def get_random_image():
	images = os.listdir('static/images/jpg')
	return random.choice(images)

@app.route('/')
def show_entries():

####
#### get collections....
	try:
		response = tcia_client.get_collection_values()
		print "**********"
		#printServerResponse(response);
		print "this section worked..."
		
		collections = []
		asdf = json.loads(response.read())
		print asdf[0].values()[0]
		print type(response.read()),"**"
		for collection in asdf:
			collections.append(collection.values()[0])
		print "**",collections

	except urllib2.HTTPError, err:
		print "Errror executing program:\nError Code: ", str(err.code), "\nMessage:", err.read()
####
####
 
	image_filepath = "static/images/jpg/"+ get_random_image()
	return render_template('index.html',image_filepath=image_filepath,collections=collections)

@app.route('/tumor')
def shasdfasdf():
	image_filepath = "static/images/jpg/"+ get_random_image()
	return render_template('index.html',image_filepath=image_filepath)

@app.route('/not_tumor')
def asjdfhohrewjg():
	image_filepath = "static/images/jpg/"+ get_random_image()
	return render_template('index.html',image_filepath=image_filepath)

#with app.




if __name__ == '__main__':
	app.run() 
