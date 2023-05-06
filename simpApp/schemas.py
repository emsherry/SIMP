from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, DOUBLE_PRECISION
from time import time


from simpApp import db


class Auth(db.Model):
    __tablename__ = "auth"

    email_id = Column(String(120), unique=True, autoincrement=True)
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

    company_id = Column(Integer, primary_key=True, autoincrement=True)
    is_active = Column(Boolean, nullable=False)
    last_updated = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<company {self.company_id},{self.is_active}>"


class Stocks(db.Model):
    __tablename__ = "stocks"

    stock_id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, db.ForeignKey("companies.company_id") ,nullable=False)
    stock_value = Column(Integer, nullable=False)
    date_published = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)
    last_updated = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return f"<stock {self.stock_id},{self.company_id},{self.stock_value},{self.is_active}"

class CompanyInformation(db.Model):
    __tablename__ = "company_information"

    company_id = Column(Integer, ForeignKey('companies.company_id'), primary_key=True)
    reg = Column(Integer, unique=True, nullable=False)
    date_established = Column(DateTime, nullable=False)
    owner_name = Column(String(20), nullable=False)
    current_floating_stocks = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False, default=0)
    last_updated = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<comp_info {self.company_id},{self.registration},{self.is_active}>"
    
class Trades(db.Model):
    __tablename__ = 'trades'

    trade_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user_info.user_id'), nullable=False)
    stock_id = Column(Integer, ForeignKey("stocks.stock_id"), nullable=False)
    buying_price = Column(Integer, nullable=False)
    date_sold = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<trade {self.trade_id},{self.user_id},{self.stock_id}>"

class News(db.Model):
    __tablename__ = "news"

    news_id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("companies.company_id"), nullable=False)
    sentiment = Column(Text, nullable=False)
    sentiment_score = Column(DOUBLE_PRECISION, nullable=False, default=0)
    last_updated = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<news {self.company_id},{self.sentiment_score}>"
