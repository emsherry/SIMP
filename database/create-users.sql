create database users with owner="fizo-neechan"
encoding="utf-8";

-- /c users


create table auth(
    email_id text unique not null,
    user_id serial primary key,
    pass varchar(128) not null,
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

grant all on wallet to admin;
grant all on auth to admin;
grant all on user_info to admin;

grant all on auth_user_id_seq to admin;
grant all on wallet_wallet_id_seq to admin;



-- TRIGGERS

-- Create trigger for auth table
CREATE OR REPLACE FUNCTION update_auth_last_updated()
RETURNS TRIGGER AS $$
BEGIN
  NEW.last_updated = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER auth_last_updated
BEFORE UPDATE ON auth
FOR EACH ROW
EXECUTE FUNCTION update_auth_last_updated();


-- Create trigger for user_info table
CREATE OR REPLACE FUNCTION update_user_info_last_updated()
RETURNS TRIGGER AS $$
BEGIN
  NEW.last_updated = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER user_info_last_updated
BEFORE UPDATE ON user_info
FOR EACH ROW
EXECUTE FUNCTION update_user_info_last_updated();


-- Create trigger for wallet table
CREATE OR REPLACE FUNCTION update_wallet_last_updated()
RETURNS TRIGGER AS $$
BEGIN
  NEW.last_updated = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER wallet_last_updated
BEFORE UPDATE ON wallet
FOR EACH ROW
EXECUTE FUNCTION update_wallet_last_updated();
