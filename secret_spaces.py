from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def start_here():
    return "Hi! This is the home page."


# route to display a simple "about" page
@app.route('/about')
def say_hello():
    return render_template("about.html")






if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)