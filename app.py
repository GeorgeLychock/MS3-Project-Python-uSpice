import os
import datetime
import math
from random import *
from random import random
from dns.rdatatype import NULL
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask.helpers import total_seconds
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

global new_rating


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_term = request.form.get("quick_search")
        print(search_term)
        return redirect(url_for("search", term=search_term))

    # obtail highest rated recipe data, limited to the top 5
    data = mongo.db.recipes.find().sort("rating", -1).limit(5)
    # obtail flavor category data
    regions = mongo.db.region.find()
    return render_template("index.html", recipes=data, regions=regions)


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
            "password": generate_password_hash(request.form.get("password")),
            "avatar_url": request.form.get("avatar")
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
    # Code reuse from Code Institute, Backend Development, Mini Project lesson
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    avitar = mongo.db.users.find_one(
        {"username": session["user"]})["avatar_url"]
    recipes = mongo.db.recipes.find(
        {"author": username}).sort("date_posted", -1)

    if session["user"]:
        return render_template(
            "profile.html", username=username, avitar=avitar, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove session cookie
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/search/<term>", methods=["GET", "POST"])
def search(term):
    if term == "All":
        search_results = mongo.db.recipes.find().limit(5)
    else:
        search_results = mongo.db.recipes.find({"recipe_region": term})
    print(search_results)
    return render_template("search.html", recipes=search_results, term=term)


@app.route("/build_recipe", methods=["GET", "POST"])
def build_recipe():
    if request.method == "POST":
        # Create ingredient lists
        ing_ids = request.form.getlist("ingredient_id")
        ing_names = request.form.getlist("ingredient_name")
        ing_quantities = request.form.getlist("ingredient_quantity")
        ing_measures = request.form.getlist("ingredient_measure")
        ing_list = []

        # Build ingredients dictionary
        for ind in range(len(ing_names)):
            ing_dict = {
                "_id": ing_ids[ind],
                "name": ing_names[ind],
                "quantity": ing_quantities[ind],
                "measure": ing_measures[ind]
            }
            ing_list.append(ing_dict)

        # Create date posted
        x = datetime.datetime.now()
        post_date = x.strftime("%x")

        # Create recipe url replacing spaces in name
        #  w/ underscores and making lowercase
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
            "rating": 0
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added to view by the entire world!")
        return redirect(url_for("recipe", ruid=ruid))

    try:
        session["user"]
        # obtail category data
        categories = mongo.db.categories.find().sort("category_name", 1)
        regions = mongo.db.region.find().sort("region_name", 1)
        measures = list(mongo.db.measures.find())
        ingredients = list(mongo.db.ingredients.find())
        return render_template(
            "build_recipe.html", categories=categories, regions=regions,
            measures=measures, ingredients=ingredients)
    except:
        flash("Please log on or register before submitting a recipe. Thanks!")
        return redirect(url_for("login"))


@app.route("/recipe/<ruid>", methods=["GET", "POST"])
def recipe(ruid):
    # Capture rating input from user
    total = 0
    inc = 0
    recipe_data_dict = dict(
        mongo.db.recipes.find_one_or_404({"recipe_uid": ruid}))

    # Create date posted
    x = datetime.datetime.now()
    post_date = x.strftime("%x")

    if request.method == "POST":
        rating_input = request.form.get("rating")
        print(f'Rating Input {rating_input}')
        existing_rating = mongo.db.ratings.find_one(
            {"ruid": ruid, "rater": session["user"]})
        if existing_rating:
            # update the existing rating
            print(f'Exiting Rating')
            mongo.db.ratings.update(
                {"_id": existing_rating["_id"]},
                {"$set": {"rating": rating_input}})
            flash("Your rating has been updated!")

            # Calculate new ratings average
            ratings = mongo.db.ratings.find({"ruid": ruid})
            for rating in ratings:
                rate_val = rating["rating"]
                total = total + int(rate_val)
                inc = inc + 1
            new_rating = round(float(total / inc), 1)

            # Update recipe db document with new ratings calc
            mongo.db.recipes.update_one(
                {"recipe_uid": ruid}, {"$set": {"rating": new_rating}})
            return redirect(url_for(
                "recipe_ratings", username=session["user"]))
        else:
            print(f'New Rating')
            rating_post = {
                "rating": int(rating_input),
                "rater": session["user"],
                "ruid": ruid,
                "post_date": post_date,
                "recipe_name": recipe_data_dict["recipe_name"]
            }
            mongo.db.ratings.insert_one(rating_post)

        ratings = mongo.db.ratings.find({"ruid": ruid})
        for rating in ratings:
            rate_val = rating["rating"]
            total = total + int(rate_val)
            inc = inc + 1
        new_rating = round(float(total / inc), 1)
        mongo.db.recipes.update_one(
            {"recipe_uid": ruid}, {"$set": {"rating": new_rating}})
        return redirect(url_for("recipe_ratings", username=session["user"]))

    recipe_data = mongo.db.recipes.find_one_or_404({"recipe_uid": ruid})
    return render_template("recipe.html", recipe=recipe_data)


@app.route("/rated_recipes", methods=["GET"])
def rated_recipes():
    # obtail highest rated recipe data
    data = mongo.db.recipes.find().sort("rating", -1)
    return render_template("rated_recipes.html", recipes=data)


@app.route("/recipe_ratings/<username>", methods=["GET"])
def recipe_ratings(username):
    ratings = mongo.db.ratings.find({"rater": username}).sort("post_date", -1)
    return render_template("recipe_ratings.html", ratings=ratings)


@app.route("/edit_recipe/<ruid>", methods=["GET", "POST"])
def edit_recipe(ruid):
    if request.method == "POST":
        # Create ingredient lists
        ing_ids = request.form.getlist("ingredient_id")
        ing_names = request.form.getlist("ingredient_name")
        ing_quantities = request.form.getlist("ingredient_quantity")
        ing_measures = request.form.getlist("ingredient_measure")
        ing_list = []

        # Build ingredients dictionary
        for ind in range(len(ing_names)):
            ing_dict = {
                "_id": ing_ids[ind],
                "name": ing_names[ind],
                "quantity": ing_quantities[ind],
                "measure": ing_measures[ind]
            }
            ing_list.append(ing_dict)

        recipe_data = mongo.db.recipes.find_one_or_404({"recipe_uid": ruid})
        # Create object to upload to db
        update = {
            "author": session["user"],
            "recipe_name": request.form.get("recipe_name"),
            "recipe_uid": ruid,
            "ingredients": ing_list,
            "recipe_region": request.form.get("recipe_region"),
            "date_posted": recipe_data["date_posted"],
            "description": request.form.get("recipe_description"),
            "preparation": request.form.get("recipe_prep"),
            "image_url":  request.form.get("recipe_image_url"),
            "image_alt":  request.form.get("recipe_image_alt"),
            "url": recipe_data["url"],
            "flavors": request.form.getlist("category"),
            "rating": 0
        }

        mongo.db.recipes.update({"recipe_uid": ruid}, update)
        flash("Recipe Updated!")
        return redirect(url_for("recipe", ruid=ruid))

    try:
        session["user"]
        # obtail flavor category data
        categories = mongo.db.categories.find().sort("category_name", 1)
        regions = mongo.db.region.find().sort("region_name", 1)
        measures = list(mongo.db.measures.find())
        ingredients = list(mongo.db.ingredients.find())
        recipe_data = mongo.db.recipes.find_one_or_404({"recipe_uid": ruid})
        return render_template(
            "edit_recipe.html", categories=categories, regions=regions,
            measures=measures, ingredients=ingredients, recipe=recipe_data)
    except:
        flash("Please log on or register before submitting a recipe. Thanks!")
        return redirect(url_for("login"))

@app.route("/delete_recipe/<ruid>")
def delete_recipe(ruid):

    mongo.db.recipes.remove({"recipe_uid": ruid})
    flash("Recipe successfully deleted.")
    return redirect(url_for("profile", username=session["user"]))

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True
    )
