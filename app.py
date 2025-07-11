import requests,re
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
    print(div["href"] + "getl.php")
    return(div["href"] + "getl.php")

def extract_static_canva_link():
    url=get_first()
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36",
    "Referer": url,}

    response = requests.get(url, headers=headers, allow_redirects=True)
    print(response)
    return response.text

@app.route('/get-canva',methods=["GET"])
def get_canva():
    result = extract_static_canva_link()
    return jsonify(result)
 
@app.route("/get-link", methods=["GET"])
def get_link():
    result = get_first()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
