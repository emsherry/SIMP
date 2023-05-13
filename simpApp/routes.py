from flask import render_template, url_for, redirect, request, session, jsonify
from simpApp import app, mailinglistSignup
import psycopg2
import bcrypt



@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
def handle_index():
    if request.method == "GET":
        return render_template('index.html')
    
    
@app.route("/home/<int:status>/<string:message>", methods=["GET"])
def handle_index_message(status, message):
    if request.method == "GET":
        return render_template("index.html", status=status, message=message)

@app.route("/newslettersignup", methods=["POST"])
def handle_newslettersignup():
    if request.method == "POST":
        email = request.form["email"]
        status = mailinglistSignup.mailingListSignup(email)

        if status == 1:
            return redirect("/home/1/Successfully signed up to our mailing list!")
        else:
            return redirect("/home/0/Newsletter signup failed...")

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
        if not session.get("uid"):
            return render_template("login.html")
        else:
            return redirect("/home")
    elif request.method == "POST":

        email = request.form["email"]
        password = request.form["password"].encode('utf-8')

        query = f"""
            select user_id , pass
            from auth 
            where email_id='{email}'
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
            
            if len(ret) == 0:
                render_template("login.html", status='failure')
            elif not bcrypt.checkpw(password, ret[1].encode('utf-8')):
                render_template("login.html", status='failure')
            else:
                session["uid"] = int(ret[0])

                return app.redirect('/home')
        except (Exception, psycopg2.Error) as e:
            print("Error: ", e)
        finally:
            if conn:
                curs.close()
                conn.close()

        return app.redirect("/login")

@app.route("/signup", methods=["GET", "POST"])
def handle_signup():
    if request.method == "GET":
        if not session.get("uid"):
            return render_template("reg.html")
        else:
            return redirect("/home")
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
            password = request.form["password"].encode('utf-8')

            salt = bcrypt.gensalt()
            password = bcrypt.hashpw(password, salt).decode("utf-8")

            insertval_auth = f"('{email}','{password}')"

            try:
                conn = psycopg2.connect(database='users', 
                        user="admin", 
                        password="simpingIsTheKeyToLife123",
                        host="localhost",
                        port='5432')
                
                curs = conn.cursor()

                curs.execute(f'insert into auth(email_id, pass) values {insertval_auth} returning user_id')
                
                uid = curs.fetchone()[0]
                insertval_info = f"({uid},'{fname}','{lname}','{email}')"
                curs.execute(f"insert into user_info(user_id, first_name, last_name, email) values {insertval_info}")

                conn.commit()
            except (Exception, psycopg2.Error) as e:
                print("Failed to enter reg data into database, Error: ", e)
                return app.redirect('/signup')
            finally:
                if conn:
                    curs.close()
                    conn.close()

            return app.redirect("/login")
        
@app.route("/logout", methods=["GET"])
def handle_logout():
    print(session)
    session.pop('uid')
    print(session)
    return app.redirect('/home')

@app.route("/stocks/<string:company_name>")
def handle_company_stocks(company_name):
    query_company_information = f"""
        select
            company_id,
            company_reg,
            date_established,
            owner_name,
            current_floating_stocks
        from company_information
        where company_name='{company_name}';
    """

    query_company_stocks = """
        select
            stock_date,
            close_price
        from market_data
        where company_id={company_id}
        order by stock_date desc;
    """

    query_prediction_data ="""
        select 
            pred_date, 
            close_prediction 
        from predictions 
        where company_id={company_id} 
        order by pred_date asc;
    """

    try:
        conn = psycopg2.connect(database='stockmarket', 
                                        user="admin", 
                                        password="simpingIsTheKeyToLife123",
                                        host="localhost",
                                        port='5432')
        cursor = conn.cursor()
        cursor.execute(query_company_information)

        data = cursor.fetchone()
        company_info = {
            'company_id': data[0],
            'company_name': company_name,
            'company_reg': data[1],
            'date_established': data[2],
            'owner_name': data[3],
            'current_floating_stocks': data[4]
        }


        cursor.execute(query_company_stocks.format(company_id=company_info['company_id']))
        data = cursor.fetchmany(30)
        labels = [i[0].strftime("%Y-%m-%d") for i in data]
        vals = [i[1] for i in data]

        cursor.execute(query_prediction_data.format(company_id=company_info['company_id']))
        data = cursor.fetchmany(5)
        pred_dates = [i[0].strftime("%Y-%m-%d") for i in data]
        pred_vals = [i[1] for i in data]


    except(Exception) as error:
        print("Error::", error)
        return "ERROR"
    finally:
        return render_template("company_stocks.html", dates=labels, vals=vals, pred_dates=pred_dates, pred_vals=pred_vals)



@app.route('/details', methods=['GET'])
def details():
    return render_template("profile.html")