from os import name
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from os.path import join, dirname, realpath, os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')


app = Flask(__name__)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
# from imageupload import save_picture


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    image = db.Column(db.String(20),default='image.png')
    orders = db.relationship('Order',backref='owner',lazy=True)
    
    def __repr__(self) -> str:
        return f"Customer:{self.username}"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    short_description = db.Column(db.String(127),nullable=False)
    description = db.Column(db.Text,nullable=False)
    image = db.Column(db.String(20),default='image.png')
    customer_id = db.Column(db.Integer,db.ForeignKey("customer.id"),nullable=False)

    def __repr__(self) -> str:
        return f"Title:{self.title}"





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


#Dashboard
@app.route("/admin")
def dashboard():
    return render_template("admin/admin.html")
@app.route("/admin/customeradd", methods=["GET","POST"])
def card_add():
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        customer = Customer(
            name = request.form['name'],
            username = request.form['username'],
            email = request.form['email'],
            image = filename,

        )
        db.session.add(customer)
        db.session.commit()
        return redirect(url_for("customeredit"))
    return render_template("admin/customeradd.html")

@app.route('/admin/customeredit')
def customeredit():
    customers = Customer.query.all()
    return render_template('admin/customeredit.html', customers=customers)
    
@app.route('/admin/customer')
def customers():
    customers = Customer.query.all()
    return render_template('admin/customer.html')
if __name__ == "__main__":
    app.run(debug=True)
