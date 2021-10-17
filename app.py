import os
import datetime
from random import *
import json
from random import random
from dns.rdatatype import NULL
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


@app.route('/')
@app.route('/index')
def index():
    # obtail highest rated recipe data
    data = mongo.db.recipes.find().sort(str("rating"), 1)
    # obtail flavor category data
    categories = mongo.db.categories.find()
    return render_template("index.html", recipes=data, categories=categories)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the username already exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        ## Future functionality: Confirm with secondary pw field
        # add new user to db
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "avitar_url": request.form.get("avitar_url").lower()
        }
        mongo.db.users.insert_one(register)

        # put user into session
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if user is in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if hashed password matches db
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome back, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    avitar = mongo.db.users.find_one(
        {"username": session["user"]})["avitar_url"]

    if session["user"]:
        return render_template("profile.html", username=username, avitar=avitar)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove session cookie
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        print("Hello brother!")
        print(request.form)
        print(request.form.get("name"))
        flash("Thanks {}, we have received your message!".format(request.form.get(
            "name")))
    return render_template("search.html")


@app.route("/build_recipe", methods=["GET", "POST"])
def build_recipe():
    if request.method == "POST":
        # Create ingredient list
        ing_names = request.form.getlist("ingredient_name")
        ing_quantities = request.form.getlist("ingredient_quantity")
        ing_measures = request.form.getlist("ingredient_measure")
        ing_list = []

        for ind in range(len(ing_names)):
            ing_dict = {
                "name": ing_names[ind],
                "quantity": ing_quantities[ind],
                "measure": ing_measures[ind]
            }
            ing_list.append(ing_dict)

        # Create date posted
        x = datetime.datetime.now()
        post_date = x.strftime("%x")

        # Create recipe url replacing spaces in name w/ underscores and making lowercase
        y = request.form.get("recipe_name")
        post_url = y.lower().replace(" ", "-")

        # Generate unique ID
        z = randint(100000, 1000000)
        ruid = "recipe" + str(z)

        # Create object to upload to db
        recipe = {
            "author": session["user"],
            "recipe_name": request.form.get("recipe_name"),
            "recipe_uid": ruid,
            "ingredients": ing_list,
            "recipe_region": request.form.get("recipe_region"),
            "date_posted": post_date,
            "description": request.form.get("recipe_description"),
            "preparation": request.form.get("recipe_prep"),
            "image_url":  request.form.get("recipe_image_url"),
            "image_alt":  request.form.get("recipe_image_alt"),
            "url": post_url,
            "flavors": request.form.getlist("category"),
            "rating": 4.7
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added to view by the entire world!")
        return redirect(url_for("recipe", ruid=ruid))
    
    try:
        session["user"]
        # obtail flavor category data
        categories = mongo.db.categories.find().sort("category_name", 1)
        regions = mongo.db.region.find().sort("region_name", 1)
        measures = list(mongo.db.measures.find())
        ingredients = list(mongo.db.ingredients.find())
        return render_template("build_recipe.html", categories=categories, regions=regions, measures=measures, ingredients=ingredients)
    except:
        flash("Please log on or register before submitting a recipe. Thanks!")
        return redirect(url_for("login"))


@app.route("/recipe/<ruid>", methods=["GET", "POST"])
def recipe(ruid):
    if request.method == "POST":
        rating = {
            "rating": 5.0,
            "rater": session["user"],
            "ruid": ruid
        }
        mongo.db.ratings.insert_one(rating)
        return redirect(url_for("rate_recipe", ruid=ruid))

    data = mongo.db.recipes.find_one_or_404({"recipe_uid": ruid})
    return render_template("recipe.html", recipe=data)


@app.route("/rate_recipe/<ruid>", methods=["GET"])
def rate_recipe(ruid):
    data = mongo.db.recipes.find_one_or_404({"recipe_uid": ruid})
    return render_template("rate_recipe.html", recipe=data)


@app.route("/edit_recipe/<url>", methods=["GET", "POST"])
def edit_recipe(url):
    # obtail flavor category data
    categories = mongo.db.categories.find().sort("category_name", 1)
    regions = mongo.db.region.find().sort("region_name", 1)
    measures = list(mongo.db.measures.find())
    ingredients = list(mongo.db.ingredients.find())
    return render_template("edit_recipe.html", categories=categories, regions=regions, measures=measures, ingredients=ingredients, url=url)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
