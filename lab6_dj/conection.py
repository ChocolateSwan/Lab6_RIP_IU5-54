import MySQLdb

class Connection:
    def __init__(self, user,password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection (self):
            return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect (self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                db = self.db,
                charset = 'utf8',
                use_unicode = True

            )
    def disconnect (self):
        if self._connection:
            self._connection.close()

class Ante:
    def __init__(self,db_connection,amount):
        self.db_connection = db_connection.connection
        self.amount = amount

    def save(self):
        c = self.db_connection.cursor()
        c.execute('INSERT INTO lab6_dj_ante_model (amount) VALUES (%s)',(self.amount,))
        self.db_connection.commit()
        c.close()

    def update(self):
        c= self.db_connection.cursor()
        c.execute('update lab6_dj_ante_model set amount = 111.1 where id = 1 ')
        self.db_connection.commit()
        c.close()

    def delete_item (self):
        c=self.db_connection.cursor()
        c.execute('delete from lab6_dj_ante_model where id = 1')
        self.db_connection.commit()
        c.close()

con = Connection('olga_user','123','bets_db')

with con:
    ante = Ante(con,201.10)
    ante.save()
    ante.delete_item()
    ante.update()