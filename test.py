import MySQLdb

db = MySQLdb.connect(
    host = "localhost",
    user = 'olga_user',
    password = "123",
    db = "second_db",
    charset = "utf8"
)

c=db.cursor()
c.execute("INSERT INTO books (name, description) VALUES (%s, %s);",('Книга', "Описание книги"))
db.commit()
c.execute("select * FROM books;")
entries = c.fetchall()
for e in entries:
    print(e)
c.close()
db.close()
