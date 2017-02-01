from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# define Classes here to represent tables


class Jugglers(Base):

    __tablename__ = 'jugglers'

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    country = Column(String, nullable=False)

    catches = Column(Integer, nullable=False)


