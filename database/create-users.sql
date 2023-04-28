create database users with owner="fizo-neechan"
encoding="utf-8";

-- /c users


create table auth(
    email_id text unique not null,
    user_id serial primary key,
    pass text not null,
    last_updated date not null default now()
);

create table user_info (
    user_id int primary key,
    first_name text not null,
    last_name text,
    email text not null,
    dob date,
    res_address text,
    last_updated date not null default now(),

    foreign key (user_id) references auth(user_id)
);

create table wallet (
    user_id int not null,
    wallet_id serial primary key,
    curr_bal int check(curr_bal>0) not null,
    is_locked boolean not null,
    last_updated date not null default now(),

    foreign key (user_id) references auth(user_id)
);