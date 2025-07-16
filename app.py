from flask import Flask,render_template,request,jsonify
from datetime import date

import json

# For secrets
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
    today = date.today()
    subject = request.form['search_subject']

    api_url = "https://newsapi.org/v2/everything?q="+subject+"&apiKey="+getapikey()
    
    response = requests.get(api_url)
    data = response.json()
    
    status = data.get('status')
    articles = data.get('articles',[])
    # TODO: Need to set a condiion for this to break if not complete, Filter for the news websites
    return render_template('submit.html',news=articles,num=data.get('totalResults'),subject=subject,date=today)

@app.route('/test_search')
def test_search():
    return render_template('test_search.html')

@app.route('/test',methods=['GET'])
def test_data():
    
    subject = request.form['search_subject']

    api_url = "https://newsapi.org/v2/everything?q="+subject+"&apiKey="+getapikey()
    
    response = requests.get(api_url)
    news_posts = response.json()    
    articles = news_posts.get('articles',[])
    
    return render_template('test.html',posts=articles)

if __name__ == '__main__':
    app.run(debug=True)
