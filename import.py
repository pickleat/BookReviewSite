import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
books = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    has_header = csv.Sniffer().has_header(f.read(1024))
    f.seek(0)
    reader = csv.reader(f)
    if has_header:
        next(reader)
    for ISBN, Title, Author, YEAR in reader:
        books.execute("INSERT INTO books (ISBN, Title, Author, Year) VALUES (:ISBN, :Title, :Author, :Year)",
         {'ISBN': ISBN, 'Title': Title, 'Author': Author, 'Year': YEAR})
        print(f"added book with {Title} by {Author} from {YEAR} with {ISBN}")
    books.commit()

if __name__ == "__main__":
    main()
