from flask import Blueprint, render_template, request, session, redirect, url_for
from .auth import authenticate
from .logger import log_event

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = authenticate(username, password)

        if user:
            session["user"] = user.username
            log_event(request.remote_addr, user.username, "Login Success")
            return redirect(url_for("main.dashboard"))
        else:
            log_event(request.remote_addr, username, "Login Failed")
            return "Login Failed"

    return render_template("login.html")


@main.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("main.login"))

    username = session["user"]
    log_event(request.remote_addr, username, "Dashboard Access")
    return render_template("dashboard.html", user=username)


@main.route("/logout")
def logout():
    username = session.get("user")
    session.clear()
    log_event(request.remote_addr, username, "Logout")
    return redirect(url_for("main.login"))