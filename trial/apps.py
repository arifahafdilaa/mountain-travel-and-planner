from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/flask-model")
def hello():
    return "Hello, World!"
