import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Medio(enum.Emun):
    DISCO = 1
    CASETE = 2
    CD = 3

class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    año = Column(Integer)
    descripcion = Column(String)
    medio = Column(Enum(Medio))
    canciones = relationship('Cancion', secondary='album_cancion')