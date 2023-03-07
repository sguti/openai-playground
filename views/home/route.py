from flask import Blueprint, render_template

home = Blueprint('home', __name__, url_prefix="/", template_folder="templates")


@home.route("/home")
@home.route("/")
def home_index():
    return render_template("home.html")
