from flask import Flask, render_template, redirect, request, flash, jsonify
from flask import session as flask_session
from model import session as model_session
from secrets import DEFAULT_SECRET_TOKEN, DEFAULT_PUBLIC_TOKEN
import model, urllib2
import os

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)
app.secret_key = "w943irtugehbdvnsckmawqoe4"
app.debug = True


## Supply the access token using an access token query parameter:
## https://api.tiles.mapbox.com/v4/{resource}.json?access_token=pk.eyJ1IjoiZWNhbyIsImEiOiJHVEFEM1NnIn0.6hb7Mp5jlFNiu22rsZkDUg

### SSL
### All API endpoint URLs support both http and https schemes. URI References in TileJSON response bodies default to HTTP regardless of the protocol used in the request. Include the ?secure querystring in the request to have resources in the response reference HTTPS endpoints.
### https://api.tiles.mapbox.com/v4/{resource}.json?secure=1


@app.route('/')
def start_here(): 
    return render_template("index.html")


# route to display a simple "about" page
@app.route('/about')
def say_hello():
    return render_template("about.html")


# loads a form for user to log in
@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


# takings user form input and checked against db to see if user exists;
# if user exists, success message flashes
# if user exists but pw is incorrect, an 'incorrect pw' messages flashes
# if user does not exist in db, then page is redirect to the 'create acct' page
@app.route("/login", methods=["POST"])
def process_login():
    """Receive the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session."""

    email = request.form['email']
    password = request.form['password']

    user = model_session.query(model.User).filter(model.User.email == email).first()
    print "args are requested"
    if user != None:
        if email == user.email and password == user.password:
            flask_session['email'] = email
            flash("Hello %s! Login successful."% (user.email))
            print "user flask session %s" % email
            return redirect("/user")
        else:
            flash("Incorrect password! Try again.")
            print "got thru first"
            return redirect("/login")

    else: 
        flash("Create an account first!")
        return redirect("/create")


# FIX ME - BE ABLE TO ACCESS THE SESSION USING JS
# THE SESSION IS A RETURN OBJECT THAT EXISTS
# ACROSS SCRIPTS --- CONSOLE.LOG Session to see what's in it
@app.route("/pushcoords", methods=["GET"])
def push_coords():
    """Receive the lat long of current user and store it in the session"""
    latlong = request.args
    latitude = request.args['lat']
    longitude = request.args['long']
    print "latlong: %s" % latlong
    print "latitide: %s" % latitude
    print "longitude: %s" % longitude

    flask_session['lat'] = latitude
    flask_session['long'] = longitude
    print "flask session: %s" % flask_session
    print "session latitide: %s" % latitude
    print "session longitude: %s" % longitude

    print "request.args = %s" % request.args
    # the result above is currently ImmutableMultiDict([('lat, u'37.7886534'), ('long, u'-122.41')])

    return "Stuff happening here!"

# TEST -- take lat long from session in the GET pushcoords route and place in 
# form template that contains mapbox api map latlong loading capability
@app.route("/pushcoords", methods=["POST"])
def load_profile_map():
    """Take user lat long and send to mapbox to populate map datapoint"""
    #function will use request.form/args (?) and place them in the URL query
    #string that will populate the map; JSON??
    #use jinga in the map html form template to populate this URL string
    pass #FIX ME --- NEED TO FIGURE OUT WHERE NEW MAP GOES


@app.route("/user", methods=["GET"])
def load_user():
    email = request.args.get('email')
    user_email = model_session.query(model.User).filter(model.User.email == email).first()
    return render_template("user.html", user_email=email)


@app.route('/create', methods=["GET"])
def create_acct():
	return render_template("create_acct.html")


@app.route("/create", methods=["POST"])
def process_acct():
	email = request.form["email"]
	password =request.form["password"]
	new_user_acct = model.User(email=email, password=password)
	model_session.add(new_user_acct)
	model_session.commit()
	flash("Your account has been succesfully added.")
	flask_session["email"] = email
	return redirect("/")

# FIX ME ---- display_images not working, 
# and images=display_images is not correct
@app.route("/list")
def list():
    all_locations = model.session.query(model.Location).all()
    display_images = model.session.query(model.Image).all()
    return render_template("list.html", locations=all_locations,
        images=display_images)


@app.route("/profile/<int:popoid>")
def load_profile(popoid):
    print "\n\n%s\n\n" %(popoid)
    info = model.session.query(model.Location).get(popoid)
    url = model.session.query(model.Image).get(popoid)
    print "info is %s" %(info)
    return render_template("profile.html", location=info, image=url)

@app.route("/map")
def load_map():
    public_key = DEFAULT_PUBLIC_TOKEN
    secret_key = DEFAULT_SECRET_TOKEN
    print public_key
    return render_template("map.html", public_token=public_key, secret_token=secret_key)






if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)