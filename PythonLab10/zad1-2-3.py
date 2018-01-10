import sqlite3

conon = sqlite3.connect('test.db')

conon.execute('''CREATE TABLE IF NOT EXISTS
BOOKS(ID INT PRIMARY KEY     NOT NULL,
       TITLE           TEXT    NOT NULL,
       AUTHOR          TEXT    NOT NULL,
       YEAR            INTEGER NOT NULL,
       ISBN            TEXT    NOT NULL);''')

conon.execute('''CREATE TABLE IF NOT EXISTS
READERS(ID INT PRIMARY KEY    NOT NULL,
       FIRSTNAME             TEXT    NOT NULL,
       LASTNAME              TEXT    NOT NULL,
       BOOK      FOREIGN KEY INT     NOT NULL,
       RETURNDATE            DATE    NOT NULL);''')


print "Utworzono tabele";

try:
    conon.execute("INSERT INTO BOOKS (TITLE, AUTHOR, YEAR, ISBN) \
          VALUES (1, 'Zew Krwi', 'Jack London', 1966, 'ABC-654' )");
    conon.execute("INSERT INTO BOOKS (TITLE, AUTHOR, YEAR, ISBN) \
          VALUES (2, 'Bialy Kiel', 'Jack London', 1972, 'ABD-134' )");
    conon.execute("INSERT INTO READERS (FIRSTNAME, LASTNAME, BOOK, RETURNDATE) \
          VALUES ('Janusz', 'Kowalski', '1', '2018-10-10' )");
    conon.commit()

    cursor = conon.execute('''SELECT * FROM BOOKS''')
    for row in cursor:
        print row

except:
    conon.rollback()

conon.close()
