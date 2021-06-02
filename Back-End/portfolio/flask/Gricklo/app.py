from os import name
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"User:{self.username}"
#Yaratmaq
# db.create_all()
# db.session.add(User(name="subhan",username='subhan' ,email="subhan@example.com"))
# db.session.commit()



# users = User.query.all()
# for user in users:
#     print(user.id,user.name)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blogdetails")
def blogdetails():
    return render_template("blogdetails.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/listing")
def listing():
    return render_template("listing.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def signup():
    return render_template("register.html")
if __name__ == "__main__":
    app.run(debug=True)
