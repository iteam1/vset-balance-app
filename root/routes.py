from flask import render_template,flash, redirect,url_for,request
from root import app
from flasgger import Swagger,swag_from

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('home.html'),200