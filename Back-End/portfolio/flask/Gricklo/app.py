from datetime import datetime
from os import name
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from os.path import join, dirname, realpath, os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads/')
app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# migrate = Migrate(app,db)

class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    phone = db.Column(db.String(25), unique=True, nullable=False)
    image = db.Column(db.String(20),default='image.png')
    orders = db.relationship('Order',backref='order',lazy=True, cascade="all,delete")
    comments =db.relationship('Comment',backref='comment',lazy=True, cascade="all,delete")
    blogs = db.relationship('Blog',backref='blog',lazy=True, cascade="all,delete")
    
    def __repr__(self) -> str:
        return f"Customer:{self.username}"

class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    customer_id = db.Column(db.Integer,db.ForeignKey("customer.id"),nullable=False)
    description = db.Column(db.Text,nullable=False)
    comment_posted=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"Comment:{self.title}"

class Blog(db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    short_description = db.Column(db.String(50),nullable=False)
    description = db.Column(db.Text, nullable=False)
    blog_posted = db.Column(db.DateTime, default=datetime.utcnow)
    image = db.Column(db.String(20), default = "default.png")
    category = db.Column(db.Integer, db.ForeignKey('blogcategory.id'), nullable=False)
    customer =db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    def __repr__(self) -> str:
        return f"Blog :{self.title}"

class BlogCategory(db.Model):
    __tablename__ = "blogcategory"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50),nullable = False)
    category =db.relationship(Blog, backref='blogcategories',lazy=True ,cascade="all,delete")
    order = db.relationship("Order", backref='orders',lazy=True ,cascade="all,delete")
    def __repr__(self) -> str:
        return f"Blog Category:{self.title}"

class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    short_description = db.Column(db.String(127),nullable=False)
    description = db.Column(db.Text,nullable=False)
    price = db.Column(db.Float,nullable=False)
    image = db.Column(db.String(20),default='image.png')
    customer_id = db.Column(db.Integer,db.ForeignKey("customer.id"),nullable=False)
    category = db.Column(db.Integer,db.ForeignKey("blogcategory.id"),nullable=False)
    def __repr__(self) -> str:
        return f"Title:{self.title}"

class Restaurant(db.Model):
    __tablename__ = "restaurant"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    location = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20),default='image.png')
    city = db.Column(db.Integer,db.ForeignKey('city.title'),nullable=False)
    
    def __repr__(self) -> str:
        return f"Customer:{self.title}"

class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),nullable=False,unique=True)
    image = db.Column(db.String(20),default='image.png')
    restaurant =db.relationship(Restaurant, backref='restaurant',lazy=True ,cascade="all,delete")
    def __repr__(self) -> str:
        return f"City:{self.title}"



@app.route("/")
def index():
    restaurants = Restaurant.query.all()
    citys = City.query.all()
    return render_template("index.html",restaurants=restaurants, citys= citys)

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
def customer_add():
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        customer = Customer(
            name = request.form['name'],
            username = request.form['username'],
            email = request.form['email'],
            phone = request.form['phone'],
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
    


#Restaurant add
@app.route("/admin/resadd", methods=["GET","POST"])
def restaurant_add():
    cities =City.query.all()
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        restaurant = Restaurant(
            title = request.form['title'],
            location = request.form['location'],
            image = filename,
            city = request.form['city']

        )
        db.session.add(restaurant)
        db.session.commit()
        return redirect(url_for("restaurant_list"))
    return render_template("admin/resadd.html", cities=cities)

@app.route('/admin/reslist')
def restaurant_list():
    restaurants = Restaurant.query.all()
    
    return render_template('admin/reslist.html', restaurants=restaurants)


@app.route('/admin/resedit/<int:id>' ,methods=["GET","POST"])
def restaurant_edit(id):
    cities =City.query.all()
    restaurants = Restaurant.query.get_or_404(id)
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        restaurants.title= request.form['title']
        restaurants.location = request.form['location']
        restaurants.image = filename
        restaurants.city = request.form['city']
        db.session.commit()
        return redirect(url_for("restaurant_list"))

    return render_template('admin/resedit.html', restaurants=restaurants , cities = cities)

@app.route('/admin/resdelete/<int:id>')
def restaurant_delete(id):
    restaurants = Restaurant.query.get_or_404(id)
    db.session.delete(restaurants)
    db.session.commit()
    return redirect(url_for("restaurant_list"))

#city add
@app.route("/admin/cityadd", methods=["GET","POST"])
def city_add():
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        city = City(
            title = request.form['title'],
            image = filename,

        )
        db.session.add(city)
        db.session.commit()
        return redirect(url_for("city_list"))
    return render_template("admin/cityadd.html")

@app.route('/admin/citylist')
def city_list():
    cities = City.query.all()
    return render_template('admin/citylist.html', cities=cities)


@app.route('/admin/cityedit/<int:id>' ,methods=["GET","POST"])
def city_edit(id):
    
    cities = City.query.get_or_404(id)
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        cities.title= request.form['title']
        cities.image = filename
        db.session.commit()
        return redirect(url_for("city_list"))

    return render_template('admin/cityedit.html',  cities = cities)

@app.route('/admin/citydelete/<int:id>')
def city_delete(id):
    cities = City.query.get_or_404(id)
    db.session.delete(cities)
    db.session.commit()
    return redirect(url_for("city_list"))

#blog
@app.route("/admin/blogadd", methods=["GET","POST"])
def blog_add():
    blogs =Blog.query.all()
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blog = Blog(
            title = request.form['title'],
            location = request.form['location'],
            image = filename,
            city = request.form['city']

        )
        db.session.add(restaurant)
        db.session.commit()
        return redirect(url_for("restaurant_list"))
    return render_template("admin/resadd.html", blogs=blogs)

@app.route('/admin/bloglist')
def blog_list():
    blogs = Blog.query.all()
    
    return render_template('admin/reslist.html', blogs=blogs )


@app.route('/admin/blogedit/<int:id>' ,methods=["GET","POST"])
def blog_edit(id):
    categories =Blog.query.all()
    blogs = Restaurant.query.get_or_404(id)
    if request.method == "POST":
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        blogs.title= request.form['title']
        blogs.location = request.form['location']
        blogs.image = filename
        blogs.city = request.form['city']
        db.session.commit()
        return redirect(url_for("restaurant_list"))

    return render_template('admin/resedit.html', blogs=blogs , categories = categories)

@app.route('/admin/resdelete/<int:id>')
def blog_delete(id):
    blogs = City.query.get_or_404(id)
    db.session.delete(blogs)
    db.session.commit()
    return redirect(url_for("blog_list"))


#blogcategory
@app.route("/admin/categoryadd", methods=["GET","POST"])
def category_add():
    if request.method == "POST":
        category = BlogCategory(
            title = request.form['title']

        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("category_list"))
    return render_template("admin/categoryadd.html")

@app.route('/admin/categorylist')
def category_list():
    categories = BlogCategory.query.all()
    return render_template('admin/categorylist.html', categories=categories)

@app.route('/admin/categoryedit/<int:id>' ,methods=["GET","POST"])
def category_edit(id):
    categories =BlogCategory.query.all()
    if request.method == "POST":
        categories.title= request.form['title']
        db.session.commit()
        return redirect(url_for("category_list"))

    return render_template('admin/categoryedit.html', categories = categories)

@app.route('/admin/categorydelete/<int:id>')
def category_delete(id):
    categories = BlogCategory.query.get_or_404(id)
    db.session.delete(categories)
    db.session.commit()
    return redirect(url_for("category_list"))

if __name__ == "__main__":
    app.run(debug=True)