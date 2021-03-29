from flask import Flask, render_template, request, session
from db import *
from otp_mail import *

app = Flask(__name__)
app.secret_key = 'a really secret super key has been set'
app.config['SESSION_TYPE'] = 'memcache'


# homepage
@app.route('/')
def site():
    return render_template("site.html")


# login page
@app.route('/login')
def login():
    return render_template("login.html")


# new user registration page
@app.route('/register')
def register():
    return render_template("register.html")


# page to handle post requests for login
@app.route('/loginres', methods=['POST'])
def loginres():
    data = {"status": "f"}
    if request.method == 'POST':

        email = request.form['email']
        r_password = request.form['password']

        if log_user_in(email, r_password):
            data["status"] = "s"

    return render_template("loginres.html", data=data)


# page to handle registration requests and set session variables
@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        data = {"status": "f"}
        name = request.form['name']
        email = request.form['email']
        r_pass = request.form['password']
        if check(email):
            session['otp'] = send_otp(email)
            session['name'] = name
            session['email'] = email
            session['password'] = r_pass
            data["status"] = "s"

        return render_template("verify.html", data=data)


# page to verify otp
@app.route('/otp.html', methods=['POST'])
def otp():
    print("in otp")
    if request.method == 'POST':
        data = {"status": 'f'}
        r_otp = int(request.form['otp'])
        if r_otp == session.get('otp'):
            print("success")
            register_user(session.get('name'), session.get('email'), session.get('password'))
            data['status'] = 's'
        return render_template('otp.html', data=data)


if __name__ == '__main__':
    app.run()
