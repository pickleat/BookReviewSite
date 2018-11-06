

-- Books Table 
CREATE table books(
    isbn varchar not null primary key UNIQUE,
    Title varchar not null,
    Author varchar not null, 
    Year int not null
);

-- Had to alter the table after the fact; used: 
ALTER TABLE books ADD UNIQUE (isbn);
ALTER TABLE books ADD primary key (isbn);
insert into books(ISBN, Title, Author, Year) values(380795272, 'Krondor: The Betrayal', 'Raymond E. Feist', '1998')


-- User Table
CREATE table users(
    username varchar not null primary key UNIQUE,
    password varchar not null, 
    id serial 
);

-- Reviews Table
CREATE table reviews(
    username varchar not null references users,
    isbn varchar not null references books,
    stars int not null,
    review varchar not null,
    UNIQUE (username, isbn)
);

-- test reviews table
insert into reviews(username, isbn, stars, review) values('andy@email.com', '0747263744', 1, 'this book was terrible');
    -- second should throw error because that book already has a review
insert into reviews(username, isbn, stars, review) values('andy@email.com', '0747263744', 2, 'this book was not as terrible');
