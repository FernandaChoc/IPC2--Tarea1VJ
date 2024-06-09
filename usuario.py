class Usuario:
      def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

      def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}"