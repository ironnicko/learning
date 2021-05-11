from flask import Flask, render_template, url_for, request, session, flash, redirect
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# secret key for sessions

app.permanent_session_lifetime = timedelta(minutes=40)
app.secret_key = os.getenv("secret")

# database initiation

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("uri")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# the SQL model to store and access


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return self.name

# Home Page


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html", content=["Nikhil", "Harini Sridhar"])

# View Data Page


@app.route("/view")
def view():
    return render_template("view.html", items=users.query.all())

# Delete Page


@app.route("/delete", methods=["GET", "POST"])
def delete():
    for i in users.query.all():
        db.session.delete(i)
    db.session.commit()
    flash("You just delelted everything", "info")
    logout()
    return render_template("view.html")


# Login Page

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["name"]
        session["user"] = user
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, None)
            db.session.add(usr)
            db.session.commit()

        flash(f"you have logged in successfully! {user}", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash(f"you have already logged in successfully", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

# User Page


@app.route("/user", methods=["GET", "POST"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!", "info")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", user=user)
    else:
        flash("You aren't logged in", "info")
        return redirect(url_for("login"))
# Logout Page


@app.route("/logout")
def logout():
    if "user" in session:
        user = session.get("user")
        flash(f"You have been logged out successfully! {user}", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
