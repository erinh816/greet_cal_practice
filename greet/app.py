from flask import Flask, request

app = Flask(__name__)

@app.get('/welcome')
def welcome_page():
    return 'welcome'

@app.get('/welcome/home')
def welcome_home():
    return 'welcome home'

@app.get('/welcome/back')
def welcome_back():
    return 'welcome back'
