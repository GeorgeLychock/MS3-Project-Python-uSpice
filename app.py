import os
import pymongo
import json
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "uSpice"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


@app.route("/")
def index():

    data = []
    collection = "recipes"

    conn = mongo_connect(MONGO_URI)

    coll = conn[DATABASE][collection]

    data = coll.find()

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
