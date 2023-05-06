create database stockMarket with owner="fizo-neechan"
encoding="utf-8";

-- \c stockMarket

create table companies (
    company_id serial primary key,
    is_active boolean not null,
    last_updated date not null default now()
);

create table stocks (
    stock_id serial primary key,
    company_id int not null references companies(company_id),
    stock_value int not null check(stock_value>0),
    date_published date not null default now(),
    is_active boolean not null default 'false',
    last_updated date default now()
);

create table company_information (
    company_id int primary key references companies(company_id),
    company_reg int unique not null,
    date_established date not null,
    owner_name text not null,
    current_floating_stocks int not null check(current_floating_stocks>=0) default 0,
    last_updated date not null default now(),
);

create table trades (
    trade_id int primary key,
    user_id int not null,
    stock_id int not null references stocks(stock_id),
    buying_price int not null check(buying_price>0),
    date_sold date not null default now()
);

create table news (
    news_id serial primary key,
    company_id int not null references companies(company_id),
    sentiment text not null,
    sentiment_score double precision not null default 0,
    last_updated date not null default now()
);
