"""
The file that holds the schema/classes
that will be used to create objects
and connect to data tables.
"""

from sqlalchemy import ForeignKey, Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from database import Base

# TODO: Complete your models

class Hike(Base):
    __tablename__ = "hikes"

    # Columns
    id = Column("id", INTEGER, primary_key=True)
    name = Column("name", TEXT, nullable = False)
    location = Column("location", TEXT, nullable = False)
    pets = Column("pets", TEXT, nullable = False)
    weather = Column("weather", TEXT, nullable = False)
    users = relationship("User", secondary = "userhikes", back_populates = "hikes")

    #Constructor
    def __init__(self, name, location, pets, weather):
        self.name = name
        self.location = location
        self.pets = pets
        self.weather = weather

class user(Base):
    __tablename__ = "users"
    # Columns
    username = Column("username", TEXT, primary_key=True)
    password = Column("password", TEXT, nullable=False)
    hikes = relationship("Hike", secondary = "userhikes", back_populates = "users")
    #Constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password


class userhike(Base):
    __tablename__ = "userhikes"

    #Columns
    id = Column("id", INTEGER, primary_key=True)
    user_id = Column("user_id", INTEGER, ForeignKey('users.username'))
    hike_id = Column("hike_id", INTEGER, ForeignKey('hikes.id'))

    