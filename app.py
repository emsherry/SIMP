from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask_migrate import Migrate

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from time import time


usr = "simp-admin"
password = "}eikQyFK6>ikM[iV"
db_conn_name = "celestial-torus-385804:us-central1:simp"
db_connstr = f"postgres://{usr}:{password}@simp?host={db_conn_name}"


app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://fizo:fizosDBProj@localhost:5432/postgres'
app.config["SQLALCHEMY_DATABASE_URI"] = db_connstr

db = SQLAlchemy(app)
migrate = Migrate(app, db)





class Auth(db.Model):
    __tablename__ = "auth"

    email_id = Column(String(120), unique=True)
    user_id = Column(Integer, primary_key=True)
    password = Column(String(60), unique=True)
    last_updated = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<auth {self.email_id},{self.user_id}>"


class UserInfo(db.Model):
    __tablename__= "user_info"

    user_id = Column(Integer, db.ForeignKey('auth.user_id'), primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    Email = Column(String(120), nullable=False)
    dob = Column(DateTime, nullable=True)
    res_address = Column(String(120), nullable=True)
    last_updated = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<user {self.user_id},{self.first_name},{self.last_name}"


class Wallet(db.Model):
    __tablename__ = "wallet"

    user_id = Column(Integer, db.ForeignKey("auth.user_id"), nullable=False)
    wallet_id = Column(Integer, primary_key=True)
    curr_bal = Column(Integer, nullable=False)
    is_locked = Column(Boolean, nullable=False)
    last_updated = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return f"<wallet {self.wallet_id},{self.curr_bal},{self.is_locked}"


class Company(db.Model):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<company {self.company_id},{self.is_active}>"


class Stocks(db.Model):
    __tablename__ = "stocks"

    stock_id = Column(Integer, primary_key=True)
    company_id = Column(Integer, db.ForeignKey("companies.company_id") ,nullable=False)
    stock_value = Column(Integer, nullable=False)
    date_published = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)
    last_updated = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return f"<stock {self.stock_id},{self.company_id},{self.stock_value},{self.is_active}"


@app.route("/")
def index():
    return render_template("index.html")

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



if __name__ == "__main__":
    app.run(debug=True)