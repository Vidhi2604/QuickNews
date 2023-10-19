from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)   #to initiate flask
@app.route('/', methods={"GET", "POST"})   #to send data from backend to frontend
def index():                #flask function

    url="https://www.businesstoday.in/technology/news"
    req=requests.get(url)
    soup=BeautifulSoup(req.content, "html.parser")
    outerdata = soup.find_all("div",class_="widget-listing", limit=7)
    finalNews = ""
    for data in outerdata:
        news = data.div.div.a["title"]
        finalNews += "\u2022 " + news + "\n"
    return render_template("index.html", News=finalNews)