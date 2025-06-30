from flask import Blueprint, render_template, redirect
from flask_login import login_required, current_user, logout_user

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
