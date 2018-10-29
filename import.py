import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
print(engine)
books = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for ISBN, Title, Author, Year in reader:
        books.execute("INSERT INTO books (ISBN, Title, Author, Year) VALUES (:ISBN, :Title, :Author, :Year)",
         {'ISBN': ISBN, 'Title': Title, 'Author': Author, 'Year': Year})
        print(f"added book with {Title} by {Author} from {Year} with {ISBN}")
    books.commit()

if __name__ == "__main__":
    main()


