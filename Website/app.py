from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import ModelHelper

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

modelHelper = ModelHelper()

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/pdf")
def pdf():
    # Return template and data
    return render_template("pdf.html")

@app.route("/works_cited")
def works_cited():
    # Return template and data
    return render_template("works_cited.html")

@app.route("/machine_learning")
def machine_learning():
    # Return template and data
    return render_template("machine_learning.html")

@app.route("/source_data")
def source_data():
    # Return template and data
    return render_template("source_data.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/tableau2")
def tableau2():
    # Return template and data
    return render_template("tableau2.html")

@app.route("/tableau3")
def tableau3():
    # Return template and data
    return render_template("tableau3.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)

    budget = float(content["budget"])
    popularity = float(content["popularity"])
    revenue = float(content["revenue"])
    runtime = float(content["runtime"])
    vote_count = float(content["vote_count"])
    genre = content["genre"]
    production_company = content["production_company"]
    production_country = content["production_country"]
    spoken_language = content["spoken_language"]
    release_year = float(content["release_year"])
    release_month = float(content["release_month"])
    release_is_weekend = int(content["release_is_weekend"])

    preds = modelHelper.makePredictions(budget, popularity, revenue, runtime, vote_count, genre, production_company, production_country, spoken_language, release_year, release_month, release_is_weekend)
    return(jsonify({"ok": True, "bad_prob": preds["bad_prob"], "good_prob": preds["good_prob"]}))


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
