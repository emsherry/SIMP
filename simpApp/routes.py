from flask import render_template, url_for, redirect, request
from simpApp import app
import psycopg2

# from simpApp.schemas import *


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template('index.html')

@app.route("/stocks", methods=["GET", "POST"])
def handle_index():
    if request.method == "POST":
        return "<h1>UNDEFINED</h1>"
    else:
        query = '''
            select
                company_name,
                f.change
            from company_information
            inner join 
            (
                select 
                    market_data.company_id,
                    change
                from market_data
                inner join (
                    select 
                        max(stock_date) as stock_date,
                        company_id
                    from market_data
                    group by company_id
                ) as f on 
                    f.company_id=market_data.company_id and f.stock_date=market_data.stock_date
            ) as f on
                f.company_id=company_information.company_id;
        '''

        conn = psycopg2.connect(database='stockmarket', 
                                user="admin", 
                                password="simpingIsTheKeyToLife123",
                                host="localhost",
                                port='5432')
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template("stocks.html", data=data)

@app.route("/contact", methods=['GET'])
def handle_contact():
    if request.method == "GET":
        return render_template("contact.html")