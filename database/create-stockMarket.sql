create database stockMarket with owner="fizo-neechan"
encoding="utf-8";

-- \c stockMarket

create table companies (
    company_id serial primary key,
    is_active boolean not null,
    last_updated date not null default now()
);

-- create table stocks (
--     stock_id serial primary key,
--     company_id int not null references companies(company_id),
--     stock_value int not null check(stock_value>0),
--     date_published date not null default now(),
--     is_active boolean not null default 'false',
--     last_updated date default now()
-- );

create table company_information (
    company_id int primary key references companies(company_id),
    company_name varchar(30) unique not null,
    company_reg int unique not null,
    date_established date not null,
    owner_name text not null,
    current_floating_stocks int not null check(current_floating_stocks>=0) default 0,
    company_description text,
    last_updated date not null default now()
);

-- create table trades (
--     trade_id int primary key,
--     user_id int not null,
--     stock_id int not null references stocks(stock_id),
--     buying_price int not null check(buying_price>0),
--     date_sold date not null default now()
-- );

create table news (
    news_id serial primary key,
    company_id int not null references companies(company_id),
    sentiment_title text not null,
    link text not null,
    sentiment_score double precision not null default 0,
    last_updated date not null default now()
);

create table predictions (
  company_id int references companies(company_id) not null,
  pred_date date not null,
  close_prediction double precision not null
)


create table market_data(
    company_id int not null references companies(company_id),
    stock_date date not null default now(),
    open_price double precision not null,
    high_price double precision not null,
    low_price double precision not null,
    close_price double precision not null,
    volume int not null,
    change double precision not null
);

create table watchlist(
  company_id int references companies(company_id) not null,
  user_id int not null
);


create user admin with password 'simpingIsTheKeyToLife123';
grant all on companies to admin;
grant all on company_information to admin;
grant all on market_data to admin;
grant all on news to admin;
grant all on stocks to admin;
grant all on trades to admin;
grant all on watchlist to admin;



-- triggers


-- Create trigger for companies table
CREATE OR REPLACE FUNCTION update_companies_last_updated()
RETURNS TRIGGER AS $$
BEGIN
  NEW.last_updated = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER companies_last_updated
BEFORE UPDATE ON companies
FOR EACH ROW
EXECUTE FUNCTION update_companies_last_updated();


-- Create trigger for company_information table
CREATE OR REPLACE FUNCTION update_company_information_last_updated()
RETURNS TRIGGER AS $$
BEGIN
  NEW.last_updated = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER company_information_last_updated
BEFORE UPDATE ON company_information
FOR EACH ROW
EXECUTE FUNCTION update_company_information_last_updated();


-- Create trigger for news table
CREATE OR REPLACE FUNCTION update_news_last_updated()
RETURNS TRIGGER AS $$
BEGIN
  NEW.last_updated = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER news_last_updated
BEFORE UPDATE ON news
FOR EACH ROW
EXECUTE FUNCTION update_news_last_updated();


-- Create trigger for market_data table
CREATE OR REPLACE FUNCTION update_market_data_last_updated()
RETURNS TRIGGER AS $$
BEGIN
  NEW.last_updated = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER market_data_last_updated
BEFORE UPDATE ON market_data
FOR EACH ROW
EXECUTE FUNCTION update_market_data_last_updated();

