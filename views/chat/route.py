from flask import Blueprint, render_template

chat = Blueprint('chat', __name__, url_prefix="/", template_folder="templates")


@chat.route("/chat")
def chat_index():
    return render_template("chat.html")
