# Load libraries
from flask import Flask, jsonify
import numpy as np
import tensorflow as tf
import requests

# instantiate flask
app = Flask(__name__)

# load the model, and pass in the custom metric function
model = tf.keras.models.load_model('recommendation_rankingbased(dim32).h5')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# define a predict function as an endpoint
@app.route("/predict/<int:id>", methods=["GET"])
def predict(id):
    test_ratings = {}
    test_mountain_ids = np.arange(1, 233)
    for mountain_id in test_mountain_ids:
        test_ratings[mountain_id] = model({
            "user_id": np.array([id]),
            "mountain_id": np.array([mountain_id])
        })
    result = [int(title) for title, score in sorted(test_ratings.items(), key=lambda x: x[1], reverse=True)[:10]]
    #

    mountain_name = []
    for i in result:
        r = requests.get('https://firestore.googleapis.com/v1beta1/projects/mountain-travel-bangkit/databases/(default)/documents/mountain/' + str(i))
        s = r.json()
        for k,v in s['fields']['Nama'].items():
            mountain_name.append(v)

    response_json = {
        "data": id,
        "prediction": result,
        "name": mountain_name
    }

    # return a response in json format
    return jsonify(response_json)


# start the flask app, allow remote connections
app.run(host='0.0.0.0')
