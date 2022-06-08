from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/getloc-api-recomendation")
def hello():
    return "Hello, World!"
