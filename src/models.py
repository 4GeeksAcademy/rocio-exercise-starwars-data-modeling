import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), index = True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), unique=True)
    password = Column(String(250), unique=True)


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    favorite_id = Column(Integer)

    user = relationship("Users")
    planet = relationship("Planets")
    vehicle = relationship("Vehicles")
    character = relationship("Character")
 

class Planets(Base):
    __tablename__ = 'planets'


    id = Column(Integer, primary_key= True)
    name = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))


class Character(Base):
    __tablename__ = 'character'


    id = Column(Integer, primary_key= True)
    name = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250), ForeignKey('Planets.id'))


class Vehicles(Base):
    __tablename__ = 'vehicles'


    id = Column(Integer, primary_key= True)
    name = Column(String(250))
    model = Column(String(250))
    passengers = Column(Integer)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
