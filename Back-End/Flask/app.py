from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')

def home():

    sayi = 10

    return render_template('index.html',number = sayi)


if __name__ == "__main__":

    app.run(debug=True)
