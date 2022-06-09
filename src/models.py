import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    second_name = Column(String(250))
    street_name = Column(String(250))
    post_code = Column(String(250), nullable=False)
    email = Column(String(250),primary_key=True)
    password = Column(Integer,primary_key=True)
    planetas_fav = Column(String,ForeignKey('planetas.id'))
    personajes_fav = Column(String,ForeignKey('personajes.id'))
    # name = Column(String(250), nullable=False)

class Inicio(Base):
    __tablename__ = 'inicio'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    # street_name = Column(String(250))
    # street_number = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_password = Column(Integer, ForeignKey('user.password'))
    user = relationship(User)

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    tamaño = Column(Integer)
    ecosistema = Column(String(250))  

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    color_pelo = Column(String)
    ecosistema = Column(String(250))
    sexo = Column(String)  

class Base_de_datos(Base):
    __tablename__ = 'base_de_datos'
    id = Column(Integer,primary_key=True)
    planetas_total= Column(Integer,ForeignKey('planetas.id')) 
    personajes_total = Column(Integer, ForeignKey('personajes.id'))   



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')