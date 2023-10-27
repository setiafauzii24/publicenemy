import requests, os
from flask import Flask, jsonify, request, json
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv() #buat baca file yg dibuat sblumnya si .env

app = Flask(__name__)
CORS(app)
v1_path = os.environ.get("V1_PATH")
port = os.environ.get("PORT")

@app.route(f"{v1_path}/hello",methods=["GET"])
def hello():
    print("BUAHAHAHAHA")
    return "Helo Panda"


@app.route(f"{v1_path}/hello",methods=["POST"])
def post():
    body = request.get_json()
    first_name = body.get("first_name")
    last_name = body.get("last_name")

    return f"inshaalah berkah {first_name} {last_name}"


app.run(host="0.0.0.0", port=port, debug=True)
