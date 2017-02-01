from DbTables import Base, Jugglers
from sqlalchemy import create_engine, select, MetaData
from sqlalchemy.orm import sessionmaker


class DB:
    def __init__(self):
        engine = create_engine('sqlite:///lab3.db', echo=False)

        # not needed since using
        # session = DBSession()
        # self.conn = engine.connect()

        # code from http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def get_all(self):
        results = self.session.query(Jugglers).all()
        return results

    def find_by_name(self, search):
        results = self.session.query(Jugglers).filter(Jugglers.name.contains(search)).all()

        return results

    def find_by_country(self, search):
        results = self.session.query(Jugglers).filter(Jugglers.country.contains(search)).all()
        return results

    def find_by_catches(self, search):
        results = self.session.query(Jugglers).filter(Jugglers.catches.contains(search)).all()
        return results

    def update(self, data):
        juggler = self.session.query(Jugglers).filter_by(id=data['id']).first()  # id is primary key
        juggler.name = data['name']
        juggler.country = data['country']
        juggler.catches = data['catches']
        self.session.commit()

    def delete(self, data):
        juggler = self.session.query(Jugglers).filter_by(id=data['id']).first()
        self.session.delete(juggler)
        self.session.commit()

    def insert(self, data):
        # example taken from http://pythoncentral.io/introductory-tutorial-python-sqlalchemy/
        new_juggler = Jugglers(name=data['name'], country=data['country'], catches=data['catches'])
        self.session.add(new_juggler)
        # save new juggler
        self.session.commit()

    def close_connection(self):
        self.session.close()
