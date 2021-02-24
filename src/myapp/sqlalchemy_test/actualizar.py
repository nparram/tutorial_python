from src.myapp.model.cancion import Cancion
from src.myapp.model.interprete import Interprete
from src.myapp.model.declarative_base import Session

if __name__ == '__main__':
  session = Session()

  cancion = session.query(Cancion).get(2)
  interprete = session.query(Interprete).get(4)

  cancion.minutos = 5
  cancion.segundos = 30
  cancion.compositor = "Pedro Pérez"
  cancion.interpretes.append(interprete)
  session.add(cancion)
  session.commit()
  session.close()