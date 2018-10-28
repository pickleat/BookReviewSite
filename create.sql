CREATE table users (
    username varchar not null,
    password varchar not null
);

CREATE table books(
    isbn varchar not null,
    Title varchar not null,
    Author varchar not null, 
    Year integer not null
);

insert into books(ISBN, Title, Author, Year) values(380795272, 'Krondor: The Betrayal', 'Raymond E. Feist', 1998)