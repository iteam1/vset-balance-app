from flask import render_template,flash, redirect,url_for,request
from root import app
from flasgger import Swagger,swag_from

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

@app.route("/")
@app.route("/home")
@app.route("/index")
@swag_from('apidocs/homepage.yml')
def home():
    return render_template('home.html'),200