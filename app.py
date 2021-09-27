import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():

    data = mongo.db.recipes.find()

    return render_template("index.html", page_title="Home", recipes=data)


@app.route("/about/<recipe_name>")
def about_recipe(recipe_name):
    recipe = {}
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == recipe_name:
                recipe = obj
    return render_template("recipe.html", recipe=recipe)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        print("Hello brother!")
        print(request.form)
        print(request.form.get("name"))
        flash("Thanks {}, we have received your message!".format(request.form.get(
            "name")))
        
    return render_template("search.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
