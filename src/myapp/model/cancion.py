from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from declarative_base import Base

class Cancion(Base):
  __tablename__ = 'cancion'

  id = Column(Integer, primary_key=True)
  titulo = Column(String)
  minutos = Column(Integer)
  segundos = Column(Integer)
  compositor = Column(String)
  interpretes = relationship('Interprete', cascade='all, delete, delete-orphan')
  albumes = relationship('Album', secondary='album_cancion')