import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the username already exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Future functionality: Confirm with secondary pw field
        # add new user to db
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put user into session
        session["user"] = request.form.get("username").lower()
        flash("Registeration Successful")
    return render_template("register.html")


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
