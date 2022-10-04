import sqlite3
from flask import render_template,flash, redirect,url_for,request, make_response
from flasgger import Swagger,swag_from
from root import app

#define a template Info Object
template = {
    "swagger":"2.0",
    "info":{
        "title":"local-app",
        "description":"API documments",
        "contact":{
            "name": "",
            "url": "http://www.swagger.io/support",
            "email": ""
        },
        "version":"0.1",
        "schemes":['http','https']
    }
}

swagger = Swagger(app,template = template)

# def balance_value():
    
@app.route("/")
@app.route("/home")
@app.route("/index")
@swag_from('apidocs/homepage.yml')
def home():
    return render_template('home.html'),200

@app.route("/api/balance")
def get_balance_value():
    conn = sqlite3.connect("./root/site.db")
    c = conn.cursor()
    c.execute("""SELECT *FROM db WHERE id = 1""")
    data = c.fetchone() # Get all row
    conn.commit()
    balance_value = data[2] # start with 1
    return balance_value
