from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')

def home():

    

    return "Home Page"

@app.route("/register")

def register():

    return "Register"


@app.route("/login/<user>")

def login(user):

    return f"Hello:{user}"


if __name__ == "__main__":

    app.run(debug=True)
