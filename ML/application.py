import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///ml.db")

@app.route("/")
def index():
    return render_template("test.html")

@app.route("/login", methods = ["GET", "POST"])
def login():

    if request.method == "POST":

        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("pass")):
            return "Wrong username and/or password", 403

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/register", methods = ['GET', 'POST'])
def register():

    if request.method == "POST":

        if request.form.get("pass") != request.form.get("confirmation pass"):
            return "Both Passwords must be same!", 403

        rows = db.execute("SELECT * FROM users")

        for row in rows:
            if request.form.get('username') == row['username']:
                return "Username already exists", 403

        try:
            values = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
                    username = request.form.get("username"), hash = generate_password_hash((request.form.get("pass"))))
        except:
            return "Registration Error", 403

        session["user_id"] = values
        return redirect("/login")

    else:
        return render_template("register.html")
