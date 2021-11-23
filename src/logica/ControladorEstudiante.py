from src.modelo.Estudiante import Estudiante
from src.modelo.declarative_base import engine, Base, session

class ControladorEstudiante():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_estudiante(self, apellidoPaterno, apellidoMaterno, nombres, elegible):

        if (apellidoPaterno == " " and apellidoMaterno == " " and nombres == " " and elegible == " "):
            return False

        busqueda = session.query(Estudiante).filter(Estudiante.apellidoPaterno == apellidoPaterno,
                                                    Estudiante.apellidoMaterno == apellidoMaterno,
                                                    Estudiante.nombres == nombres,
                                                    Estudiante.elegible == elegible).all()
        if len(busqueda) == 0:
            estudiante = Estudiante(apellidoPaterno=apellidoPaterno, apellidoMaterno=apellidoMaterno, nombres=nombres,
                                    elegible=elegible)
            session.add(estudiante)
            session.commit()
            return True
        else:
            return False