import os
from flask import Flask, render_template, redirect, flash
from flask import url_for, request, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from bson.json_util import dumps

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'hit_the_slopes'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

mongo = PyMongo(app)


@app.route('/')
@app.route('/show_index')
def show_index():
    return render_template("index.html")


@app.route('/sign_up_page', methods=['GET', 'POST'])
def sign_up_page():
    return render_template("sign_up.html")


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in_page():
    return render_template("sign_in.html")


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == "POST":
        users = mongo.db.users
        name = users.find_one({'name': request.form["name"]})
        if name is None:
            password = generate_password_hash(request.form["password"])
            users.insert_one(request.form.to_dict())
            session['name'] = request.form["name"]
            flash("Welcome, " + session['name'] + "!")
            return redirect(url_for('trips'))
        else:
            flash("This username already exists, please choose another one")
            return redirect(url_for('sign_up_page'))
    return render_template('trips.html', active='signed')


@app.route('/sign_in')
def sign_in():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form["name"]})
        if existing_user:
            if check_password_hash(existing_user["password"], 
                                    request.form["password"]):
                flash("Welcome back, " + existing_user["name"])
                session["name"] = existing_user["name"] 
                return redirect(url_for('trips'))
            '''
            else:
                flash("Wrong password. Try again.")
                return redirect(url_for('sign_in'))
        else:
            flash("Wrong name. Try again.")
            return redirect(url_for('sign_in'))
    '''
    return redirect(url_for('trips'))


@app.route('/user_account', methods=['POST'])
def user_account():
    return render_template("user_account.html", users=mongo.db.users.find())


@app.route('/trips')
def trips():
    return render_template("trips.html", trips=mongo.db.trips.find())


@app.route('/ski_resorts')
def ski_resorts():
    return render_template("skiresorts.html", skiresorts=mongo.db.skiresorts.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)