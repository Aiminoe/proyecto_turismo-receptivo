import csv
import json
import requests
import sqlite3

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = sqlalchemy.create_engine("sqlite:///origen_y_destino.db")
base = declarative_base()

#crear tabla
class Data (base):
    __tablename__ = "Info"
    id = Column(String, primary_key=True)
    provincia_de_destino = Column(String)
    pais_de_residencia = Column(String)
    turistas_no_residentes = Column(Integer)
   
    def __repr__(self):
        return f"Datos: id {self.id}, provincia de destino {self.provincia_de_destino}, pais de residencia {self.pais_de_residencia}, turistas no residentes {self.turistas_no_residentes}"

#crear db
def create_schema():
  base.metadata.drop_all(engine)

    
  base.metadata.create_all(engine)

# crear insert de objetos para la db
def insert(provincia_de_destino,pais_de_residencia,turistas_no_residentes):
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear un nuevo producto
    new_data = Data(provincia_de_destino=provincia_de_destino,pais_de_residencia=pais_de_residencia,turistas_no_residentes=turistas_no_residentes)
   
    # Agregar el nuevo producto a la DB
    session.add(new_data)
    session.commit()

   
   
# insertar objetos de csv a la tabla de a db   
def fill():
    archivo= "origen_y_destinos_visitados.csv"
    with open(archivo) as csvfile:
        data = list(csv.DictReader(csvfile))

    for row in data:
        
        insert(row['provincia_de_destino'],row ['pais_de_residencia'],row ['turistas_no_residentes'])









if __name__ == '__main__':

    create_schema()    

    

    fill()

