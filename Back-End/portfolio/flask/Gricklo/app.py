from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():

    return render_template("app/index.html")

@app.route("/login")
def login():
    return render_template("app/login.html")

@app.route("/signup")
def signup():
    return render_template("app/signup.html")

@app.route("/blog")
def blog():
    return render_template("app/blog.html")

@app.route("/blogdetails")
def blogdetails():
    return render_template("app/blogdetails.html")

@app.route("/contact")
def contact():
    return render_template("app/contact.html")

@app.route("/listing")
def listing():
    return render_template("app/listing.html")

@app.route("/about")
def about():
    return render_template("app/about.html")
if __name__ == "__main__":
    app.run(debug=True)