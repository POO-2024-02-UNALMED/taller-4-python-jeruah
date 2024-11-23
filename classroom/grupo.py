from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None): #inicializa estudiantes como lista vacia, asignaturas tambien
        if asignaturas is None:
            self._asignaturas = []
        else:
            self._asignaturas = asignaturas
        if estudiantes is None:
            self.listadoAlumnos = []
        else:
            self.listadoAlumnos = estudiantes
        self._grupo = grupo

    # faltan los ** de kwargs.
    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
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

