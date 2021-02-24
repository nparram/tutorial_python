from src.myapp.model.cancion import Cancion
from src.myapp.model.declarative_base import Session

if __name__ == '__main__':
  session = Session()
  cancion2 = session.query(Cancion).get(2)
  session.delete(cancion2)
  session.commit()
  session.close()