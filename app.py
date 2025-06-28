import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
def get_first():
    url="https://bingotingo.com/best-social-media-platforms/"
    response = requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    div= soup.find("a",class_="su-button su-button-style-soft su-button-wide")
    print(div["href"])
    return(div["href"])

 
@app.route("/get-link", methods=["GET"])
def get_link():
    result = get_first()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
