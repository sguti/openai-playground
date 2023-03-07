from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

# Import views
from views.home import home
from views.chat import chat

# Import apis
from apis.messages import messages_api

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(chat)
app.register_blueprint(messages_api)


@app.route('/')
def index():
    return redirect('/home', code=302)


if __name__ == '__main__':
    app.run()
