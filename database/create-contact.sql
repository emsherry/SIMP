create table contactus(
    contact_id serial primary key,
    fname varchar(30) not null,
    lname varchar(30) not null,
    email varchar(120) not null,
    phnum varchar(12) not null,
    question text not null,
    preferance varchar(5) not null
);


grant all on contactus to admin;
grant all on contactus_contact_id_seq to admin;