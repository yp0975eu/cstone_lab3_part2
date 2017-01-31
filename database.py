import sqlite3
import logging


class DB:
    database_name = "lab3.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.database_name)

        self.cursor = self.connection.cursor()

    def create_tables(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS chainsaw_records
                (name TEXT NOT NULL,
                 country TEXT NOT NULL,
                 catches INT NOT NULL
                 );''')
            self.connection.commit()

            logging.info("Database created")

        except sqlite3.Error as er:
            print(er)

    def get_all(self):
        query = '''SELECT rowid, name, country, catches FROM chainsaw_records'''
        try:
            self.cursor.execute(query)

            return self.cursor.fetchall()

        except sqlite3.Error as er:
            print('Select Error', er)

    def find_by_name(self, search):
        query = '''SELECT * FROM chainsaw_records WHERE name LIKE ? '''
        return self.select(query, search)

    def find_by_country(self, search):
        query = '''SELECT * FROM chainsaw_records WHERE country LIKE ? '''
        return self.select(query, search)

    def find_by_catches(self, search):
        query = '''SELECT * FROM chainsaw_records WHERE catches LIKE ? '''
        return self.select(query, search)

    def close_connection(self):

        self.connection.close()

    def update_prepare(self, new_data):

        query = '''UPDATE chainsaw_records SET name = ?, country = ?, catches = ? WHERE rowid = ?'''
        self.update(query, new_data)

    def delete_prepare(self, id):

        query = '''DELETE FROM chainsaw_records WHERE rowid = ?'''

        self.delete(query, id)

    def delete(self, query, data):
        try:

            self.cursor.execute(query, (data,))

            self.connection.commit()

        except sqlite3.Error as er:

            print("delete error", er)

    def update(self, query, data):
        # TODO: store in a dictionary so the code is more readable. ex: data['name'], data['id']
        try:
            self.cursor.execute(query, (data[1], data[2], data[3], data[0]))
            self.connection.commit()

        except sqlite3.Error as er:

            print("update error", er)

    # data must be a tuple
    def insert(self, data: tuple):

        query = '''INSERT INTO chainsaw_records VALUES(?, ?, ?)'''

        try:

            self.cursor.execute(query, data)

            self.connection.commit()

        except sqlite3.Error as er:

            print("insert error", er)

    def select(self, query, search):
        try:
            self.cursor.execute(query, ('%' + search + '%',))

            return self.cursor.fetchall()

        except sqlite3.Error as er:
            print('Select Error', er)
