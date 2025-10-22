from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/upload")
def upload():
    return render_template("upload.html")

@main.route("/calculator")
def calculator():
    return render_template("calculator.html")

@main.route("/profile")
def profile():
    return render_template("profile.html")
