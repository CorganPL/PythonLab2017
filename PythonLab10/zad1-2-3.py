import sqlite3

conon = sqlite3.connect('test.db')

conon.execute('''CREATE TABLE IF NOT EXISTS BOOKS
        (ID INT PRIMARY KEY     NOT NULL,
        TITLE           TEXT    NOT NULL,
        AUTHOR          TEXT    NOT NULL,
        YEAR            INTEGER NOT NULL,
        ISBN            TEXT    NOT NULL)''')

conon.execute('''CREATE TABLE IF NOT EXISTS READERS
        (ID     INT     PRIMARY KEY    NOT NULL,
        FIRSTNAME             TEXT    NOT NULL,
        LASTNAME              TEXT    NOT NULL)''')

conon.execute('''CREATE TABLE IF NOT EXISTS BOOKS_READERS
        (BOOK_ID     INT,
        READER_ID   INT,
        FOREIGN KEY(BOOK_ID)    REFERENCES  BOOKS(ID),
        FOREIGN KEY(READER_ID)  REFERENCES  READERS(ID))''')


print "Utworzono tabele"

try:
    conon.execute("INSERT INTO BOOKS VALUES (1, 'Zew Krwi', 'Jack London', 1966, 'ABC-654' )");
    conon.execute("INSERT INTO BOOKS VALUES (2, 'Bialy Kiel', 'Jack London', 1972, 'ABD-134' )");
    conon.execute("INSERT INTO READERS VALUES (1, 'Janusz', 'Kowalski')");
    conon.execute("INSERT INTO BOOKS_READERS VALUES (2, 1)");
    conon.commit()

    cursor = conon.execute('''SELECT * FROM BOOKS''')
    for row in cursor:
        print row

except:
    conon.rollback()

conon.close()
