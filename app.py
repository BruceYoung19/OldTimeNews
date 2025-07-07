from flask import Flask,render_template,request,jsonify
from datetime import date

import json
import configparser
import httpx
import requests


def getapikey():
    config = configparser.ConfigParser()
    config.read("secrets.ini")
    return config["news"]["api_key"]

app = Flask(__name__)

@app.route('/')
def home():
    today = date.today()
    return render_template('main.html', today_date=today)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    subject = request.form['search_subject']
    news_data = news.searchInput(subject)
    
    articles = news_data.get('articles',[])
    # TODO: Need to set a condiion for this to break if not complete.
    
    return render_template('submit.html',news=articles)

@app.route('/test',methods=['GET'])
def test_data():
    api_url = "https://newsapi.org/v2/everything?q="+"Tesla"+"&apiKey="+getapikey()
    
    response = requests.get(api_url)
    news_posts = response.json()    
    # print(news_posts)
    articles = news_posts.get('articles',[])
    return render_template('test.html',posts=articles)

if __name__ == '__main__':
    app.run(debug=True)
