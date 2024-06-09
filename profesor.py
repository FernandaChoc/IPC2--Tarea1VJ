from usuario import Usuario

class Profesor(Usuario):
    def __init__(self, nombre, curso, codigo, profesion):
                self.nombre = nombre
                self.curso = curso
                self.codigo = codigo
                self.profesion = profesion

    def __str__(self):
     return f"Nombre: {self.nombre}, Curso: {self.curso}, Código: {self.codigo}, Profesión: {self.profesion}"