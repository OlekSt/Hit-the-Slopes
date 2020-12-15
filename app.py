import os
from flask import Flask, render_template, redirect, flash
from flask import url_for, request, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from datetime import date


from os import path
# import file where username and password of MongoDB is saved
if path.exists("env.py"):
    import env

# create instance of flask
app = Flask(__name__)
# add configuration to Flask app
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# create an instance of Pymongo with app object being pushed as argument
mongo = PyMongo(app)


@app.route('/')
# redirect if the logo is clicked either to index.html
# if not logged, or to trips.hmtl if logged in
@app.route('/show_index')
def show_index():
    if "user" in session:
        return redirect(url_for('trips'))
    else:
        return render_template("index.html")


@app.route('/sign_up_page', methods=['GET', 'POST'])
def sign_up_page():
    return render_template("sign_up.html")


@app.route('/sign_in_page', methods=['GET', 'POST'])
def sign_in_page():
    return render_template("sign_in.html")


@app.route('/add_user', methods=['POST'])
def add_user():
    users = mongo.db.users
    if request.method == "POST":
        name = users.find_one(
            {'name': request.form.get("name").lower().capitalize()})
        if name is None:
            user = {
                "name": request.form.get("name").lower().capitalize(),
                "password": generate_password_hash(
                                request.form.get("password")),
                "gender": request.form.get("gender"),
                "ageRange": request.form.get("ageRange"),
                "city": request.form.get("city"),
                "avatar": request.form.get("avatar")
            }
            mongo.db.users.insert_one(user)
            session['user'] = request.form.get("name").lower().capitalize()
            flash("Welcome, " + session['user'] + "!")
            return redirect(url_for('trips'))
        else:
            flash("This username already exists, please choose another one.")
            return redirect(url_for('sign_up_page'))
    return render_template(
            'trips.html',
            active='signedIn',
            user=user)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one(
            {'name': request.form.get("name").lower().capitalize()})
        if existing_user:
            if check_password_hash(
             existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("name").lower().capitalize()
                logged_user = session["user"]
                flash("Welcome back, " + logged_user)
                return redirect(url_for('trips'))
            else:
                flash("Wrong password. Try again.")
                return redirect(url_for('sign_in_page'))
        else:
            flash("Wrong name. Try again.")
            return redirect(url_for('sign_in_page'))
    return render_template(
            'trips.html',
            active='signedIn',
            logged_user=logged_user)


@app.route('/user_account', methods=['POST'])
def user_account():
    return render_template(
            "user_account.html",
            users=mongo.db.users.find())


@app.route('/trips', methods=['GET', 'POST'])
def trips():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else:
        # to display trip started current/today's date
        today = date.today().strftime("%Y.%m.%d")
        trips = trips = mongo.db.trips.find({"from": {"$gte": today}})
        # sort trips by enddate too
        trips = sorted(trips,
                        key=lambda i: (i['from'], i['to']),
                        reverse=False)
        trips = list(trips)
        skiresorts = list(mongo.db.skiresorts.find())
        users = list(mongo.db.users.find())
        for trip in trips:
            trip_owner = mongo.db.trips.find_one('user')
        return render_template(
                "trips.html",
                skiresorts=skiresorts,
                trips=trips,
                users=users,
                trip_owner=trip_owner,
                active='signedIn')


@app.route('/contact_me')
def contact_me():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else:
        return render_template(
                "contact_me.html",
                active='signedIn')


# for searching through trips by ski resorts' names,
# and start/end dates
@app.route('/search_trips', methods=['GET', 'POST'])
def search_trips():
    query = request.form.get("query").lower().capitalize()
    query_from = request.form.get("query_from")
    query_to = request.form.get("query_to")
    skiresorts = mongo.db.skiresorts
    trips = mongo.db.trips
    users = mongo.db.users
    query_in_db = skiresorts.find_one(  # check if ski resort in DB
            {'location_name': request.form.get("query").lower().capitalize()})
    if query and query_from and query_to:  # search by place, & dates from & to
        if query_in_db:
            trips = mongo.db.trips.find({
                    "$text": {"$search": query},
                    "from": {"$gte": query_from},
                    "to": {"$lte": query_to}
                    })
            flash("Trips to: " + query + ", between: " +
                  query_from + " - " + query_to)
        else:  # if skiresort spelt wrongly in search field
            trips = mongo.db.trips.find({
                    "from": {"$gte": query_from},
                    "to": {"$lte": query_to}
                    })
            flash("Wrong name, or no such ski resort!..")
            flash(" Trips between: " + query_from + " - " + query_to)
    elif query_from and query_to:  # search by start/end dates of trips
        trips = mongo.db.trips.find({
                "from": {"$gte": query_from},
                "to": {"$lte": query_to}
                })
        flash("Trips between: " + query_from + " - " + query_to)
    elif query and query_from:  # search by a place and a starting date
        if query_in_db:
            trips = mongo.db.trips.find({
                    "$text": {"$search": query},
                    "from": {"$gte": query_from}
                    })
            flash("Trips to: " + query + ", starting: " + query_from)
        else:  # if skiresort spelt wrongly in search field
            trips = mongo.db.trips.find({
                    "from": {"$gte": query_from}
                    })
            flash("Wrong name, or no such ski resort!..")
            flash("Trips starting: " + query_from)
    elif query and query_to:  # search by a place & an ending date
        if query_in_db:
            trips = mongo.db.trips.find({
                    "$text": {"$search": query},
                    "to": {"$lte": query_to}
                    })
            flash("Trips to: " + query + ", till: " + query_to)
        else:  # if skiresort spelt wrongly in search field
            trips = mongo.db.trips.find({
                    "to": {"$lte": query_to}
                    })
            flash("Wrong name, or no such ski resort!..")
            flash("Trips till: " + query_to)
    elif query:      # search by a place
        if query_in_db:
            trips = mongo.db.trips.find({"$text":
                                        {"$search": query}})
            flash("Trips to: " + query)
        else:
            # to display trip started current/today's date
            today = date.today().strftime("%Y.%m.%d")
            trips = mongo.db.trips.find({
                "from": {"$gte": today}})
            flash("Wrong name, or no such ski resort!")
    elif query_from:     # search by a starting date
        trips = mongo.db.trips.find({"from":
                                    {"$gte": query_from}})
        flash("Trips starting: " + query_from)
    elif query_to:     # search by a ending date
        trips = mongo.db.trips.find({"to": {"$lte": query_to}})
        flash("Trips till: " + query_to)
    else:
        flash("No search parameters were chosen.")
        redirect(url_for('trips'))
        users = list(mongo.db.users.find())
        skiresorts = list(mongo.db.skiresorts.find())
        # to display trip started current/today's date
        today = date.today().strftime("%Y.%m.%d")
        trips = mongo.db.trips.find({
                "from": {"$gte": today}})
        trips = sorted(trips,
                       key=lambda i: (i['from'], i['to']),
                       reverse=False)
    users = list(mongo.db.users.find())
    skiresorts = list(mongo.db.skiresorts.find())
    trips = sorted(trips,
                   key=lambda i: (i['from'], i['to']),
                   reverse=False)
    return render_template(
        "trips.html",
        skiresorts=skiresorts,
        trips=trips,
        users=users,
        active='signedIn')


@app.route('/add_trip')
def add_trip():
    return render_template(
        'add_trip.html',
        skiresorts=mongo.db.skiresorts.find(),
        active='signedIn')


@app.route('/edit_trip/<trip_id>', methods=['GET', 'POST'])
def edit_trip(trip_id):
    trip = mongo.db.trips.find_one({'_id': ObjectId(trip_id)})
    return render_template(
        'edit_trip.html',
        skiresorts=mongo.db.skiresorts.find(),
        trip=trip,
        active='signedIn')


@app.route('/update_trip/<trip_id>', methods=['GET', 'POST'])
def update_trip(trip_id):
    trip = mongo.db.trips.find_one({'_id': ObjectId(trip_id)})
    for item in trip:
        if request.form.get(item) is None:
            mongo.db.trips.update_one(
                {'_id': ObjectId(trip_id)},
                {"$set":
                    {item: trip[item]}})
        else:
            mongo.db.trips.update_one(
                    {'_id': ObjectId(trip_id)},
                    {"$set":
                        {item: request.form.get(item)}})
            if request.form.get('skiresort'):
                skiresort = mongo.db.skiresorts.find_one(
                    {"$text": {"$search": request.form['skiresort']}})
                skiresort_id = skiresort['_id']
                mongo.db.trips.update_one(
                    {'_id': ObjectId(trip_id)},
                    {"$set":
                        {'location_name': request.form.get('skiresort'),
                        'skiresort_id': skiresort_id}})
    flash(session['user'] + "! We've updated your trip!")
    return redirect(url_for('trips'))


@app.route('/insert_trip', methods=['GET', 'POST'])
def insert_trip():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else:
        skiresort = mongo.db.skiresorts.find_one(
                {"$text": {"$search": request.form['skiresort']}})
        skiresort_id = skiresort['_id']
        if request.method == "POST":
            trips = mongo.db.trips
            trips.insert_one({
                'user': session['user'],
                'location_name': request.form['skiresort'],
                'skiresort_id': skiresort_id,
                'from': request.form['from'],
                'to': request.form['to'],
                'adults': request.form['adults'],
                'kids': request.form['kids'],
                'ski_snowboard': request.form['ski_snowboard'],
                'other_info': request.form['other_info'],
            })
            flash(session['user'] + "! We've added your trip!")
        return redirect(url_for('trips'))


# to prevent a user from deleting trips created by other users
@app.route('/delete_trip/<trip_id>')
def delete_trip(trip_id):
    mongo.db.trips.delete_one({'_id': ObjectId(trip_id)})
    flash(session['user'] + ", we've deleted your trip!")
    return redirect(url_for('trips'))


@app.route('/ski_resorts')
def ski_resorts():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else:
        return render_template(
            "ski_resorts.html",
            skiresorts=mongo.db.skiresorts.find(),
            active='signedIn')


# search through ski resorts
@app.route('/search_ski_resorts', methods=['GET', 'POST'])
def search_ski_resorts():
    query = request.form.get("query").lower().capitalize()
    skiresorts = list(mongo.db.skiresorts.find({"$text": {"$search": query}}))
    if skiresorts:
        return render_template(
            "ski_resorts.html",
            skiresorts=skiresorts,
            active='signedIn')
    else:
        flash("Wrong name or the ski resort is not registered.")
        return render_template(
            "ski_resorts.html",
            skiresorts=skiresorts,
            active='signedIn')


@app.route('/add_skiresort')
def add_skiresort():
    return render_template('add_skiresort.html', active='signedIn')


@app.route('/insert_skiresort', methods=['POST'])
def insert_skiresort():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else:
        if request.method == "POST":
            skiresorts = mongo.db.skiresorts
            skiresort_in_db = skiresorts.find_one({
                'location_name':
                request.form.get("location_name").lower().capitalize()
                })
            if skiresort_in_db:
                query = request.form.get("location_name").lower().capitalize()
                flash("Ski resort is already registered.")
                skiresorts = list(mongo.db.skiresorts.find(
                                    {"$text": {"$search": query}}))
                return render_template(
                    "ski_resorts.html",
                    skiresorts=skiresorts,
                    active='signedIn')
            else:
                skiresorts.insert_one({
                    'user': session['user'],
                    'location_name':
                        request.form['location_name'].lower().capitalize(),
                    'description': request.form['description'],
                    'website': request.form['website'],
                    'map': request.form['map'],
                    'night': request.form['night'],
                    'glacier': request.form['glacier'],
                    'thumbnail': request.form['thumbnail'],
                    'other_info': request.form['other_info'],
                })
                flash(session['user'] + "! We've added your ski resort!")
                return redirect(url_for('ski_resorts'))
            return render_template(
                "ski_resorts.html",
                skiresorts=mongo.db.skiresorts.find(),
                active='signedIn')


@app.route('/edit_skiresort/<skiresort_id>', methods=['GET', 'POST'])
def edit_skiresort(skiresort_id):
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else:
        return render_template(
            'edit_skiresort.html',
            skiresort=mongo.db.skiresorts.find_one(
                {'_id': ObjectId(skiresort_id)}
                ),
            active='signedIn')


@app.route('/update_skiresort/<skiresort_id>', methods=['GET', 'POST'])
def update_skiresort(skiresort_id):
    skiresort = mongo.db.skiresorts.find_one({'_id': ObjectId(skiresort_id)})
    for item in skiresort:
        if request.form.get(item) is None:
            mongo.db.skiresorts.update_one(
                {'_id': ObjectId(skiresort_id)},
                {"$set":
                    {item: skiresort[item]}})
        else:
            mongo.db.skiresorts.update_one(
                    {'_id': ObjectId(skiresort_id)},
                    {"$set":
                        {item: request.form.get(item)}})
    flash(session['user'] + "! We've updated your ski resort!")
    return redirect(url_for('ski_resorts'))


@app.route('/delete_skiresort/<skiresort_id>')
def delete_skiresort(skiresort_id):
    mongo.db.skiresorts.delete_one({'_id': ObjectId(skiresort_id)})
    flash(session['user'] + ", we've deleted your ski resort!")
    return redirect(url_for('ski_resorts'))


@app.route('/sign_out')
def sign_out():
    [session.pop(key) for key in list(session.keys())]
    return redirect(url_for('show_index'))


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
