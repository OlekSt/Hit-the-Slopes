import os
from flask import Flask, render_template, redirect, request, url_for, request, flash, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'hit_the_slopes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/show_index')
def show_index():
    return render_template("index.html")


@app.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")


@app.route('/sign_in')
def sign_in():
    return render_template("sign_in.html")


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    users = mongo.db.users
    users.insert_one(request.form.to_dict())
    return redirect(url_for('user_account'))


@app.route('/user_account', methods=['POST'])
def user_account():
    return render_template("user_account.html", users=mongo.db.users.find())


@app.route('/get_trips')
def get_trips():
    return render_template("trips.html", trips=mongo.db.trips.find())


@app.route('/get_locations')
def get_locations():
    return render_template("locations.html", locations=mongo.db.locations.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)