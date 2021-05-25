from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')

def home():

    

    return "Home Page"

@app.route("/register")

def register():

    return "Register"


@app.route("/<color>")

def color(color):

    return f"<body style='background-color:{color};'> </body>"






if __name__ == "__main__":

    app.run(debug=True)
