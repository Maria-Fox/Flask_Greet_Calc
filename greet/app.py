from flask import Flask

app = Flask (__name__)

@app.route("/welcome")
def welcome_user():
    return "Welcome"

@app.route("/home")
def home_page():
    return "Welcome Home"

@app.route("/welcome/back")
def welcome_back():
    return "Welcome back"

