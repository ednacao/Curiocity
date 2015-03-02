from flask import Flask, render_template, redirect, request, flash
from flask import session as flask_session
from model import session as model_session
from secrets import DEFAULT_SECRET_TOKEN, DEFAULT_PUBLIC_TOKEN
import model, urllib2

"""api_token = DEFAULT_SECRET_TOKEN
map_id = ecao.la8h2i58"""

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)
app.secret_key = 'thisisasecretkey'


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


# NEED TO RE-DO -- FROM RATINGS EXERCISE
# 
@app.route("/login", methods=["POST"])
def process_login():
    """TODO: Receive the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session."""

    email = request.form['email']
    password = request.form['password']

    user = model_session.query(model.User).filter(model.User.email == email).first()
    if user != None:
        if email == user.email and password == user.password:
            flask_session['email'] = email
            flash("Hello %s! Login successful."% (user.email))
            return redirect("/all_users")
        else:
            flash("Incorrect password! Try again.")
            return redirect("/login")
    else: 
        flash("Create an account first!")
        return redirect("/create")


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
@app.route("/new")
def new():
    all_locations = model.session.query(model.Location).all()
    display_images = model.session.query(model.Image).all()
    return render_template("new.html", locations=all_locations,
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
    return render_template("map.html")





if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)