import os
from flask import Flask, render_template, redirect, flash
from flask import url_for, request, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId


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
        name = users.find_one({'name': request.form.get("name")})
        if name is None:
            user = {
                "name": request.form.get("name"),
                "password": generate_password_hash(request.form.get("password")),
                "gender": request.form.get("gender"),
                "ageRange": request.form.get("ageRange"),
                "from": request.form.get("from"),
                "avatar": request.form.get("avatar")
            }
            mongo.db.users.insert_one(user)
            session['user'] = request.form["name"]
            flash("Welcome, " + session['user'] + "!")
            return redirect(url_for('trips'))
        else:
            flash("This username already exists, please choose another one")
            return redirect(url_for('sign_up_page'))
    return render_template(
            'trips.html',
            active='signedIn',
            user=user)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form["name"]})
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("name")
                flash("Welcome back, " + session["user"])
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
            user=session["user"])


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
        trips = mongo.db.trips.find().sort("from", 1)
        trips = list(trips)
        skiresorts = list(mongo.db.skiresorts.find())
        users = list(mongo.db.users.find())
        return render_template(
                "trips.html",
                skiresorts=skiresorts,
                trips=trips,
                users=users,
                active='signedIn')

# for searching through trips by ski resorts' names,
# and dates of trips starting and finishing at
@app.route('/search_trips', methods=['GET', 'POST'])
def search_trips():
    query = request.form.get("query")
    query_from = request.form.get("query_from")
    query_to = request.form.get("query_to")
    if query and query_from and query_to:  # search by place, & dates from & to
        trips = mongo.db.trips.find({
                "$text": {"$search": query},
                "from": {"$gte": query_from},
                "to": {"$lte": query_to}
                }).sort("from", 1)  # to sort in chronological order
        flash("Trips to: "+query+". Between: "+query_from+" & "+query_to)
    elif query_from and query_to:  # search by starting & ending dates of trips
        trips = mongo.db.trips.find({
                "from": {"$gte": query_from},
                "to": {"$lte": query_to}
                }).sort("from", 1)
        flash("Trips between: " + query_from + " & " + query_to)
    elif query and query_from:  # search by a place and a starting date
        trips = mongo.db.trips.find({
                "$text": {"$search": query},
                "from": {"$gte": query_from}
                }).sort("from", 1)
        flash("Trips to: " + query + ". Starting: " + query_from)
    elif query and query_to:  # search by a place & an ending date
        trips = mongo.db.trips.find({
                "$text": {"$search": query},
                "to": {"$lte": query_to}
                }).sort("from", 1)
        flash("Trips to: " + query + ". From: " + query_to)
    elif query:                                 # search by a place
        trips = mongo.db.trips.find({"$text": {"$search": query}}).sort("from",1)
        flash("Trips to: " + query)
    elif query_from:                            # search by a starting date
        trips = mongo.db.trips.find({"from": {"$gte": query_from}}).sort("from",1) 
        flash("Trips starting: " + query_from)
    elif query_to:                              # search by a ending date
        trips = mongo.db.trips.find({"to": {"$lte": query_to}}).sort("from", 1)
        flash("Trips till: " + query_to)
    else:
        redirect(url_for('trips'))
    users = list(mongo.db.users.find())
    skiresorts = list(mongo.db.skiresorts.find())
    return render_template("trips.html", 
                            skiresorts=skiresorts,
                            trips=trips,
                            users=users, active='signedIn')


@app.route('/add_trip')
def add_trip():
    return render_template('add_trip.html',
                            skiresorts=mongo.db.skiresorts.find(), 
                            active='signedIn')


@app.route('/edit_trip/<trip_id>', methods=['GET', 'POST'])
def edit_trip(trip_id):
    trip = mongo.db.trips.find_one({'_id': ObjectId(trip_id)})
    trip_owner = trip['user']
    if session['user'] == trip_owner:
        return render_template('edit_trip.html',
                                skiresorts=mongo.db.skiresorts.find(),
                                trip=mongo.db.trips.find_one({'_id': ObjectId(trip_id)}),
                                active='signedIn')
    else:
        return redirect(url_for('no_permission'))


@app.route('/update_trip/<trip_id>', methods=['GET', 'POST'])
def update_trip(trip_id):
    trip = mongo.db.trips.find_one({'_id': ObjectId(trip_id)})
    if request.form.get('skiresort'):
        mongo.db.trips.update(
            {'_id': ObjectId(trip_id)},
            {'user': session['user'],
            'location_name': request.form.get('skiresort'),
            'from': request.form.get('from'),
            'to': request.form.get('to'),
            'adults': request.form.get('adults'),
            'kids': request.form.get('kids'),
            'ski_snowboard': request.form.get('ski_snowboard'),
            'other_info': request.form.get('other_info')}
        )
    else:
        mongo.db.trips.update(
            {'_id': ObjectId(trip_id)},
            {'user': session['user'],
            'location_name': trip['location_name'],
            'from': request.form.get('from'),
            'to': request.form.get('to'),
            'adults': request.form.get('adults'),
            'kids': request.form.get('kids'),
            'ski_snowboard': request.form.get('ski_snowboard'),
            'other_info': request.form.get('other_info')}
        )  
    flash(session['user'] + "! We've updated your trip!")
    return redirect(url_for('trips'))


@app.route('/insert_trip', methods=['GET', 'POST'])
def insert_trip():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else:
        if request.method == "POST":
            trips = mongo.db.trips
            trips.insert_one({
                'user': session['user'],
                'location_name': request.form['skiresort'],
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
    trip = mongo.db.trips.find_one({'_id': ObjectId(trip_id)})
    trip_owner = trip['user']
    if session['user'] == trip_owner:
        mongo.db.trips.remove({'_id': ObjectId(trip_id)})
        flash(trip_owner + ", we've deleted your trip!")
        return redirect(url_for('trips'))
    else:
        return redirect(url_for('no_permission'))


@app.route('/ski_resorts')
def ski_resorts():
    if "user" not in session:
        return redirect(url_for('sign_in_page'))
    else:
        return render_template("ski_resorts.html", 
                                skiresorts=mongo.db.skiresorts.find(), 
                                active='signedIn')

# search through ski resorts
@app.route('/search_ski_resorts', methods=['GET', 'POST'])
def search_ski_resorts():
    query = request.form.get("query")
    skiresorts = list(mongo.db.skiresorts.find({"$text": {"$search": query}}))
    return render_template("ski_resorts.html", 
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
                'location_name': request.form["location_name"]
                })
            if skiresort_in_db:
                flash("Ski resort is already registered.")
                return render_template(
                    "ski_resorts.html",
                    skiresorts=mongo.db.skiresorts.find(),
                    active='signedIn')
            else:
                skiresorts.insert_one({
                    'location_name': request.form['location_name'],
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


# If any of "night", "glacier", or "thumbnail" are not updated
# to keep what was previously saved in DB,
# otherwise it gets lost after editing and saving
@app.route('/update_skiresort/<skiresort_id>', methods=['GET', 'POST'])
def update_skiresort(skiresort_id):
    skiresort = mongo.db.skiresorts.find_one({'_id': ObjectId(skiresort_id)})
    mongo.db.skiresorts.update(
            {'_id': ObjectId(skiresort_id)},
            {'location_name': request.form.get('location_name'),
                'description': request.form.get('description'),
                'website': request.form.get('website'),
                'map': request.form.get('map'),
                'other_info': request.form.get('other_info')}
            )
    if (request.form.get('night') and
            request.form.get('glacier') and
            request.form.get('thumbnail')):
        mongo.db.skiresorts.update(
            {'_id': ObjectId(skiresort_id)},
            {'night': request.form.get('night'),
            'glacier': request.form.get('glacier'),
            'thumbnail': request.form.get('thumbnail')}
            )
    elif (request.form.get('glacier') and request.form.get('thumbnail')):
        mongo.db.skiresorts.update(
            {'_id': ObjectId(skiresort_id)},
            {'night': skiresort['night'],
            'glacier': request.form.get('glacier'),
            'thumbnail': request.form.get('thumbnail')}
            )
    elif (request.form.get('night') and request.form.get('thumbnail')):
        mongo.db.skiresorts.update(
            {'_id': ObjectId(skiresort_id)},
            {'night': request.form.get('night'),
            'glacier': skiresort['glacier'],
            'thumbnail': request.form.get('thumbnail')}
            )
    elif (request.form.get('night') and request.form.get('glacier')):
        mongo.db.skiresorts.update(
            {'_id': ObjectId(skiresort_id)},
            {'night': request.form.get('night'),
            'glacier': request.form.get('glacier'),
            'thumbnail': skiresort['thumbnail']}
            )
    elif request.form.get('night'):
        mongo.db.skiresorts.update(
            {'_id': ObjectId(skiresort_id)},
            {'night': request.form.get('night'),
            'glacier': skiresort['glacier'],
            'thumbnail': skiresort['thumbnail']}
            )
    elif request.form.get('glacier'):
        mongo.db.skiresorts.update(
            {'_id': ObjectId(skiresort_id)},
            {'night': skiresort['night'],
                'glacier': request.form.get('glacier'),
                'thumbnail': skiresort['thumbnail']}
            )
    elif request.form.get('thumbnail'):
        mongo.db.skiresorts.update(
            {'_id': ObjectId(skiresort_id)},
            {'night': skiresort['night'],
            'glacier': skiresort['glacier'],
            'thumbnail': request.form.get('thumbnail')}
            )
    return redirect(url_for('ski_resorts'))


@app.route('/delete_skiresort/<skiresort_id>')
def delete_skiresort(skiresort_id):
    mongo.db.skiresorts.remove({'_id': ObjectId(skiresort_id)})
    return redirect(url_for('ski_resorts'))


@app.route('/sign_out')
def sign_out():
    [session.pop(key) for key in list(session.keys())]
    return redirect(url_for('show_index'))


# No permission page
@app.route('/no_permission')
def no_permission():
    return render_template(
            "no_permission.html",
            active='signedIn')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)