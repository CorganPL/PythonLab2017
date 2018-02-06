from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Books(Base):
    __tablename__ = "BOOKS"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    TITLE = Column(String)
    AUTHOR = Column(String)
    YEAR = Column(Integer)
    ISBN = Column(String)

class Readers(Base):
    __tablename__ = "READERS"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    FIRSTNAME = Column(String)
    LASTNAME = Column(String)

class Books_Readers(Base):
    __tablename__ = "BOOKS_READERS"
    BOOK_ID = Column(Integer, ForeignKey(Books.ID))
    READER_ID = Column(Integer, ForeignKey(Readers.ID))

def addBook(session):
    title = raw_input("Tytul: ")
    author = raw_input("Autor: ")
    year = raw_input("Rok wydania: ")
    isbn = raw_input("ISBN: ")
    newBook = Books(TITLE = title, AUTHOR = author, YEAR = year, ISBN = isbn)
    session.add(newBook)
    session.commit()

def addReader(session):
    fname = raw_input("Imie: ")
    lname = raw_input("Nazwisko: ")
    newReader = Readers(FIRSTNAME = fname, LASTNAME = lname)
    session.add(newReader)
    session.commit()

engine = create_engine("sqlite:///example db", echo = True )
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
