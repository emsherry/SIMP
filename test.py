import bcrypt
from flask import Flask, request, redirect, render_template, url_for, session
import os


app  = Flask(__name__)


@app.route("/login")
def login():

    session["logged_in"] = True
    session["user_id"] = 1234
    return "logged in"

@app.route('/', methods=['GET'])
def index ():

    print( session.get("logged_in"))
    print( session.get("user_id") )


    return "ok"



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0', port=5000)