from usuario import Usuario 

class Estudiante:
    def __init__(self, nombre, curso, carnet, carrera):
        self.nombre = nombre
        self.curso = curso
        self.carnet = carnet
        self.carrera = carrera

    def __str__(self):
        return f"Nombre: {self.nombre}, Curso: {self.curso}, Carnet: {self.carnet}, Carrera: {self.carrera}"
