from flask import Blueprint

messages_api = Blueprint('messages_api', __name__, url_prefix="/api/messages")


@messages_api.route("/", methods=["POST", "HEAD", "OPTIONS"])
def messages_post():
    return {
        "name": "sudip"
    }


@messages_api.route("/", methods=["GET", "HEAD", "OPTIONS"])
def messages_get():
    return {
        "name": "get"
    }
