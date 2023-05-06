from flask import render_template, url_for, redirect, request
from simpApp import app

from simpApp.schemas import *


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        # return render_template(url_for("templates","index.html"),)
        # return "????whiff"
        return render_template('index.html')

@app.route("/stocks", methods=["GET", "POST"])
def handle_index():
    if request.method == "POST":
        return "<h1>UNDEFINED</h1>"
    else:
        res = Stocks.query.where(Stocks.company_id == 1).where(Stocks.is_active)
        result = [{
            "stock_id": r.stock_id,
            "company_id": r.company_id,
            "is_active": r.is_active,
        } for r in res]
        print(result)
        return render_template("stocks.html")
