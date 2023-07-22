import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
import pickle
import urllib.request
import json
import requests
app = Flask(__name__)

@app.route('/')
def home():

    return render_template("index.html")

@app.route('/predict',methods=['GET'])
def predict():


    '''
    For rendering results on HTML GUI
    '''
    exp = float(request.args.get('exp'))


    X=[[exp]]
    # Serialize the data into json and send the request to the model
    payload = {'data': json.dumps(X)}
    y_predict = requests.post('http://127.0.0.1:5000/regression', data=payload).json()

    # Make array from the list
    prediction = np.array(y_predict)
    print("Salary is", y_predict)
    return render_template('index.html', prediction_text='Regression Model  has predicted salary for given experinace is : {}'.format(prediction))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)