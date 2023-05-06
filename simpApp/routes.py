from flask import render_template, url_for, redirect, request
from simpApp import app
import psycopg2

# from simpApp.schemas import *


@app.route("/", methods=["GET"])
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
            stock_id,
            stock_value,
            date_published
        from stocks
        inner join company_information
            on stocks.company_id=company_information.company_id
        '''

        q2  = "select * from companies"



        conn = psycopg2.connect(database='stockmarket', 
                                user="admin", 
                                password="simpingIsTheKeyToLife123",
                                host="localhost",
                                port='5432')
        cursor = conn.cursor()
        cursor.execute(q2)
        print(cursor.fetchall())

        cursor.close()
        conn.close()

        return render_template("stocks.html")
