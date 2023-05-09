from flask import render_template, url_for, redirect, request
from simpApp import app
import psycopg2


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template('index.html')

@app.route("/stocks", methods=["GET", "POST"])
def handle_stocks():
    if request.method == "POST":
        # ! todo add new company
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
        try:
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
        except:
            data = []
        finally:
            return render_template("stocks.html", data=data)

@app.route("/contact", methods=['GET', 'POST'])
def handle_contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        phNum = request.form["phNum"]
        question = request.form["question"]
        preference = request.form["preference"]

        data = f"('{fname}', '{lname}', '{email}', '{phNum}', '{question}', '{preference}')"
        query = f"insert into contactus(fname, lname, email, phnum, question, preferance) values {data}"
        
        try:
            conn = psycopg2.connect(database='maintainance', 
                    user="admin", 
                    password="simpingIsTheKeyToLife123",
                    host="localhost",
                    port='5432')
            curs = conn.cursor()
            curs.execute(query)

            conn.commit()
        except (Exception, psycopg2.Error) as e:
            print("Failed database connection, Error: ", e)
        finally:
            if conn:
                curs.close()
                conn.close()

        return app.redirect("/index")
    
@app.route("/login", methods=["GET", "POST"])
def handle_login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        query = f"""
            select user_id 
            from auth 
            where email_id='{email}' and pass='{password}'
        """

        try:
            conn = psycopg2.connect(database='users', 
                    user="admin", 
                    password="simpingIsTheKeyToLife123",
                    host="localhost",
                    port='5432')
            curs = conn.cursor()
            curs.execute(query)
            ret = curs.fetchone()
            print(ret)

            if len(ret) == 0:
                render_template("login.html", status='failure')
            else:
                uid = ret[0]
                return app.redirect(f'/index')
        except (Exception, psycopg2.Error) as e:
            print("Failed database connection, Error: ", e)
        finally:
            if conn:
                curs.close()
                conn.close()

        return app.redirect("/login")


    


@app.route("/signup", methods=["GET", "POST"])
def handle_signup():
    if request.method == "GET":
        return render_template("reg.html")
    elif request.method == "POST":

        if request.form["re_password"] != request.form["password"]:
            return render_template("reg.html", status='failure', message="Passwords do not match")
        else:
            name = request.form["name"]
            name = name.split()
            fname = name[0]
            name.pop(0)
            lname = ' '.join(name)
            email = request.form["email"]
            password = request.form["password"]

            insertval_auth = f"('{email}','{password}')"

            try:
                conn = psycopg2.connect(database='users', 
                        user="admin", 
                        password="simpingIsTheKeyToLife123",
                        host="localhost",
                        port='5432')
                
                curs = conn.cursor()
                curs.execute(f'insert into auth(email_id, pass) values {insertval_auth}')
                curs.execute(f"select user_id from auth where email_id='{email}'")
                
                uid = curs.fetchone()[0]
                insertval_info = f"({uid},'{fname}','{lname}','{email}')"
                curs.execute(f"insert into user_info(user_id, first_name, last_name, email) values {insertval_info}")

                conn.commit()
            except (Exception, psycopg2.Error) as e:
                print("Failed to enter reg data into database, Error: ", e)
            finally:
                if conn:
                    curs.close()
                    conn.close()

            return app.redirect("/login")
        
@app.route("/stcks")
def stcks():
    return render_template("stcks.html")

@app.route("/stcks", methods=["GET", "POST"])
def getStcks():
    query = "select * from market_data where company_id = 1;"

    try:    
        conn = psycopg2.connect(database='stockmarket', 
                                        user="admin", 
                                        password="simpingIsTheKeyToLife123",
                                        host="localhost",
                                        port='5432')
        cursor = conn.cursor()
        cursor.execute(query)
        return jsonify(cursor.fetchone()[0])
    except(Exception) as error:
        print(error)

