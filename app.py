from flask import Flask, render_template, request
from db import *

app = Flask(__name__)


@app.route('/')
def site():
    return render_template("site.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/loginres', methods=['POST'])
def loginres():
    if request.method == 'POST':
        data = {"status": "f"}
        email = request.form['email']
        password = request.form['password']

        if log_user_in(email, password):
            data["status"] = "s"

    return render_template("loginres.html", data=data)


@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        data = {"status": "f"}
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(name, email, password)
        if register_user(name, email, password):
            data["status"] = "s"

        return render_template("verify.html", data=data)


if __name__ == '__main__':
    app.run()
