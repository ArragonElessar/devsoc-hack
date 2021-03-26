from flask import Flask, render_template, request, session
from db import *
from otp_mail import *

app = Flask(__name__)
app.secret_key = 'a really secret super key has been set'
app.config['SESSION_TYPE'] = 'memcache'


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
        if check(email):
            session['otp'] = send_otp(email)
            session['name'] = name
            session['email'] = email
            session['password'] = password
            data["status"] = "s"

        return render_template("verify.html", data=data)


@app.route('/otp.html', methods=['POST'])
def otp():
    print("in otp")
    if request.method == 'POST':
        data = {"status": 'f'}
        otp = int(request.form['otp'])
        print("recieved otp")
        print(otp)
        if otp == session.get('otp'):
            print("success")
            register_user(session.get('name'), session.get('email'), session.get('password'))
            data['status'] = 's'
        return render_template('otp.html', data=data)


if __name__ == '__main__':
    app.run()
