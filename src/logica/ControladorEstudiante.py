import random

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

    def editar_estudiante(self, idEstudiante, apellidoPaterno, apellidoMaterno, nombres, elegible):
        busqueda = session.query(Estudiante).filter(Estudiante.apellidoPaterno == apellidoPaterno,
                                                    Estudiante.apellidoMaterno == apellidoMaterno,
                                                    Estudiante.nombres == nombres,
                                                    Estudiante.elegible == elegible,
                                                    Estudiante.idEstudiante != idEstudiante).all()
        if len(busqueda) == 0:
            estudiante = session.query(Estudiante).filter(Estudiante.idEstudiante == idEstudiante).first()
            estudiante.apellidoPaterno = apellidoPaterno
            estudiante.apellidoMaterno = apellidoMaterno
            estudiante.nombres = nombres
            estudiante.elegible = elegible
            session.commit()
            return True
        else:
            return False

    def eliminar_estudiante(self, idEstudiante):
        try:
            estudiante = session.query(Estudiante).filter(Estudiante.idEstudiante == idEstudiante).first()
            session.delete(estudiante)
            session.commit()
            return True
        except:
            return False

    def dar_estudiante(self):
        estudiantes = [elem.__dict__ for elem in
                       session.query(Estudiante).all()]
        return estudiantes

    def dar_estudiante_por_idEstudiante(self, idEstudiante):
        return session.query(Estudiante).get(idEstudiante).__dict__

    def seleccionar_Estudiante(self):
        listaEstudiantes = session.query(Estudiante).filter(Estudiante.elegible == True).all()

        return random.choice(listaEstudiantes)