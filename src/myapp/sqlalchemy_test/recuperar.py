from src.myapp.model.album import Album, Medio
from src.myapp.model.cancion import Cancion
from src.myapp.model.declarative_base import Session

if __name__ == '__main__':
    session = Session()
    canciones = session.query(Cancion).all()

    print('Las canciones almacenadas son:')
    for cancion in canciones:
        print("Titulo: " + cancion.titulo + " (00:" +
              str(cancion.minutos) + ":" +
              str(cancion.segundos) + ")")

        print("Intérpretes")
        for interprete in cancion.interpretes:
            print(" - " + interprete.nombre)

        for album in cancion.albumes:
            print(" -- Presente en el album: " + album.titulo)

        print("")

    print('Los álbumes almacenados en discos son:')
    albumes = session.query(Album).filter(Album.medio == Medio.DISCO).all()
    for album in albumes:
        print("Album: " + album.titulo)

    session.close()