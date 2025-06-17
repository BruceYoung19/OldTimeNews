import requests
import json
import configparser
import httpx

def getapikey():
    config = configparser.ConfigParser()
    config.read("secrets.ini")
    return config["news"]["api_key"]

def searchInput(query):
    link = "https://newsapi.org/v2/everything?q="+query+"&apiKey="+getapikey()
    search_news(link)

def search_news(link):
    response = httpx.get(link)
    return organize_data(response.json())

def organize_data(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text
    print(link)

