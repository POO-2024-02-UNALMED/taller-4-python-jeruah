from classroom.asignatura import Asignatura

class Grupo:
    grado = 12

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]): #inicializa estudiantes como lista vacia, asignaturas tambien
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    # faltan los ** de kwargs.
    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    # Crear un metodo que permita ver las asignaturas de un grupo
    def getAsignaturas(self):
        return self._asignaturas

