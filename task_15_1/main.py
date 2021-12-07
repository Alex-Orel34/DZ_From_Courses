import sqlite3
import CRUD

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///Products.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Products(Base):
    __tablename__ = 'Products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(FLOAT)
    quantity = Column(Integer)
    comment = Column(String)

    def __init__(self, name=0, price=0.0, quantity=0, comment=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.comment = comment


Base.metadata.create_all(engine)
k = int(input('Want start? Take 1\n'))
while k != 0:
    k = int(input(
        'If you want to insert new product put 1, if you want to read information from your BD put 2, if Update put 3, if delete 4, else put 0\n'))
    if k == 1:
        CRUD.insert()
    elif k == 2:
        CRUD.read()
    elif k == 3:
        idd = int(input('by what id you want update?\n'))
        quantity = int(input())
        CRUD.update_by_id(idd, quantity)
    elif k == 4:
        idd = int(input('by what id you want update?\n'))
        CRUD.delete_by_id(idd)
