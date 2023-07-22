from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np
import json
import urllib.request
import pickle
# code to initiate the flask app and API.
app = Flask(__name__)
api = Api(app)
# creates a request parser to parse arguments that will be sent with the request.
#data is sent in a JSON serialized format and name the key as data
# Create parser for the payload data
parser = reqparse.RequestParser()
parser.add_argument('data')

# Define how the api will respond to the post requests
class linearregression(Resource):
    def post(self):
        args = parser.parse_args()
        X = np.array(json.loads(args['data']))
        prediction = model.predict(X)
        return jsonify(prediction.tolist())

api.add_resource(linearregression, '/regression')

if __name__ == '__main__':
    # Load model
    url = "https://github.com/deepakmoud/Internship-Linear-regression/raw/main/linearregression.pkl"
    # Download the pickle file
    response = urllib.request.urlopen(url)

    # Load the pickle file
    model = pickle.load(response)
#with open('model.pickle', 'rb') as f:
        #model = pickle.load(f)

    app.run(debug=True)
