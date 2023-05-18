from flask import Flask, render_template
from flask import url_for
from flask import request

app  = Flask(__name__)

# @app.route('/index/')
# @app.route('/index/<name>')
# def hello(name=None):
#     return render_template('index.html',name=name)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def pg_about():
    return render_template('about.html')

@app.route("/jewelery")
def pg_jewelery():
    return render_template("jewelery.html")

@app.route("/contact")
def pg_contact():
    return render_template("contact.html")

@app.route("/login")
def pg_login():
    return render_template("login.html")


@app.route("/sign-up")
def pg_signup():
    return render_template("sign-up.html")
@app.route("/Forgot-Password")
def pg_for():
    return render_template("Forgot-Password.html")

# with app.test_request_context():
#     # print(url_for(''))
#     print(url_for('about'))
#     print(url_for('jewelery'))

if __name__ == '__main__':
    app.run(debug=True)


