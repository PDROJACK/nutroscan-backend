from flask import Flask, request
from detect import predict_class
import os
import urllib3
from tensorflow.keras.models import load_model
import json

http = urllib3.PoolManager()

directory = "./files"
if not os.path.exists(directory):
    os.makedirs(directory)

app = Flask(__name__)

API_KEY = "MueGQISzUxbcZut0ihEcb0oo6FVZ2JEdN2DQBlUQ"
URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

# Route to detect and send the food name 
@app.route('/detect', methods=['POST'])
def detect():
    response = {}
    image = request.files['image']
    img = "./files/"+image.filename
    image.save(img)
    predicted = predict_class(img)
    name = predicted

    res = http.request('GET', URL+'?query='+name+'&API_KEY='+API_KEY)

    data = json.loads(res.data.decode('utf-8'))

    response["food"] = name
    if data["totalHits"] == 0:
        response["foodNutrients"] = "not found"
    else:    
        response["foodNutrients"] = data["foods"][0]["foodNutrients"]
    return response


@app.route('/readlabel', methods=['POST'])
def readLabel():
    res = {}
    image = request.files['image']
    os.system("tessaract ", )
    return res