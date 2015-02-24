from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

ENGINE = create_engine("sqlite:///popos.db", echo=True)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key = True)
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=True)

    def __repr__(self):
      return "<name=%s address=%s>" % (self.name, self.address)



def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///popos.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()


def main():
    """In case we need this for something"""

if __name__ == "__main__":
    main()