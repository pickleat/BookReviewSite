CREATE table users (
    username varchar not null,
    password varchar not null
);

-- Books Table 
CREATE table books(
    isbn varchar not null,
    Title varchar not null,
    Author varchar not null, 
    Year integer not null
);

insert into books(ISBN, Title, Author, Year) values(380795272, 'Krondor: The Betrayal', 'Raymond E. Feist', 1998)



-- User Table
CREATE table users(
    username varchar not null UNIQUE,
    password varchar not null, 
    id serial 
);