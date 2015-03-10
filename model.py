from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

ENGINE = create_engine("sqlite:///popos.db", echo=True)
session = scoped_session(sessionmaker(bind=ENGINE, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    def __repr__(self):
        return "<email=%s password=%s>" %(self.email, self.password)


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key = True)
    name = Column(String(128), nullable=False)
    address = Column(String(128), nullable=False)
    description = Column(String(666), nullable=True)
    hours = Column(String(128), nullable=True)
    seating_info = Column(String(128), nullable=True)
    food_info = Column(String(128), nullable=True)
    restrooms = Column(String(128), nullable=True)
    food_yn = Column(String(3), nullable=True)
    seating_yn = Column(String(3), nullable=True)
    profile_longitude = Column(Integer, nullable=False)
    profile_latitude = Column(Integer, nullable=False)


    def __repr__(self):
      return "<name=%s address=%s>" % (self.name, self.address)


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key = True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=True)
    url = Column(String(128), nullable=True)

    location = relationship("Location",
                backref=backref("images", order_by=id))



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