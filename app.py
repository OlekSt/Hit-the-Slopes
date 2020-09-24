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
    if "user" not in session:
        return render_template("index.html")
    else: 
        return render_template("trips.html", trips=mongo.db.trips.find(), active='signedIn')


@app.route('/sign_up_page', methods=['GET', 'POST'])
def sign_up_page():
    return render_template("sign_up.html")


@app.route('/sign_in_page', methods=['GET', 'POST'])
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
    return render_template('trips.html', active='signedIn', password=password)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form["name"]})
        
        if existing_user:
            if existing_user['password'] == request.form["password"]:
                session["user"] = existing_user["name"]
                flash("Welcome back, " + existing_user["name"])
                return redirect(url_for('trips'))
            else:
                flash("Wrong password. Try again.")
                return redirect(url_for('sign_in'))
        else:
            flash("Wrong name. Try again.")
            return redirect(url_for('sign_in'))
    return render_template('trips.html', active='signedIn')


@app.route('/user_account', methods=['POST'])
def user_account():
    return render_template("user_account.html", users=mongo.db.users.find())


@app.route('/trips')
def trips():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else:
        return render_template("trips.html", trips=mongo.db.trips.find(), active='signedIn')


@app.route('/ski_resorts')
def ski_resorts():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else: 
        return render_template("skiresorts.html", skiresorts=mongo.db.skiresorts.find(), active='signedIn')


@app.route('/add_skiresort', methods=['POST'])
def add_skiresort():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else: 
         if request.method == "POST":
            skiresorts = mongo.db.skiresorts
            skiresort_in_db = skiresorts.find_one({'location_name': request.form["location_name"]})
            if skiresort_in_db:
                flash("Ski resort is already registered.")
                return render_template("skiresorts.html", skiresorts=mongo.db.skiresorts.find(), active='signedIn')
            else:
                skiresorts.insert_one({
                    'location_name': request.form['location_name'],
                    'description': request.form['description'],
                    'website': request.form['website'],
                    'spring': request.form['spring'],
                    'autumn': request.form['autumn'],
                    'night': request.form['night'],
                    'glacier': request.form['glacier'],
                    'thumbnail': request.form['thumbnail'],
                    'other_info': request.form['other_info'],
                })
                flash("We've added your ski resort!")
                return redirect(url_for('ski_resorts'))
            return render_template("skiresorts.html", skiresorts=mongo.db.skiresorts.find(), active='signedIn')


@app.route('/sign_out')
def sign_out():
    [session.pop(key) for key in list(session.keys())]
    return redirect(url_for('show_index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)