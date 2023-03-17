from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
from modelHelper import ModelHelper
import numpy as np
import os

#init app and class
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

# Route to render index.html template
@app.route("/about")
def about():
    # Return template and data
    return render_template("about_us.html")

# Route to render index.html template
@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/tableau2")
def tableau2():
    # Return template and data
    return render_template("tableau2.html")

# POST REQUEST LISTENER
@app.route("/makePredictions", methods=["POST"])
def makePrediction():
    content = request.json["data"]
    print(content)

    # parse
    sex_flag = int(content["sex_flag"])
    age = float(content["age"])
    fare = float(content["fare"])
    familySize = int(content["familySize"])
    p_class = int(content["p_class"])
    embarked = content["embarked"]

    prediction = modelHelper.makePredictions(sex_flag, age, fare, familySize, p_class, embarked)
    print(prediction)

    return(jsonify({"ok": True, "prediction": str(prediction)}))



#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)