from profesor import Profesor
from estudiantes import Estudiante

profesores = []
estudiantes = []

def menu():
    while True:
        print(" ____________________________________________________")
        print("|                                                    |")
        print("|                   Menú Principal                   |")
        print("|____________________________________________________|")
        print("|1. CRUD de Profesores                               |")
        print("|2. CRUD de Estudiantes                              |")
        print("|3. Salir                                            |")
        print("|____________________________________________________|")
        print()
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crud_profesores()
        elif opcion == "2":
            crud_estudiantes()
        elif opcion == "3":
            print("Hasta luego")
            break
        else:
            print("Opción no válida, intente nuevamente.")

def crud_profesores():
    while True:
        print(" ____________________________________________________")
        print("|                                                    |")
        print("|                 CRUD de Profesores                 |")
        print("|____________________________________________________|")
        print("|1. Crear Profesor                                   |")
        print("|2. Leer Profesores                                  |")
        print("|3. Actualizar Profesor                              |")
        print("|4. Eliminar Profesor                                |")
        print("|5. Salir al menú principal                          |")
        print("|____________________________________________________|")
        print()
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_profesor()
        elif opcion == "2":
            leer_profesores()
        elif opcion == "3":
            actualizar_profesor()
        elif opcion == "4":
            eliminar_profesor()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intente nuevamente.")

def crear_profesor():
    global profesores
    print(" ____________________________________________________")
    print("|                                                    |")
    print("|                   Crear Profesor                   |")
    print("|____________________________________________________|")
    print()
    nombre = input("Ingrese el nombre del profesor: ")
    curso = input("Ingrese el curso del profesor: ")
    codigo = input("Ingrese el código del profesor: ")
    profesion = input("Ingrese la profesión del profesor: ")
    profesor = Profesor(nombre, curso, codigo, profesion)
    profesores.append(profesor.__dict__)
    print("Profesor creado con éxito.")
    1

def leer_profesores():
    global profesores
    print(" ____________________________________________________")
    print("|                                                    |")
    print("|                      Profesores                    |")
    print("|____________________________________________________|")
    print()
    if len(profesores) == 0:
        print("No hay profesores registrados.")
    else:
        for profesor in profesores:
            json_string = f'''{{
    "nombre": "{profesor["nombre"]}",
    "curso": "{profesor["curso"]}",
    "codigo": "{profesor["codigo"]}",
    "profesion": "{profesor["profesion"]}"
}}'''
            print(json_string)

def actualizar_profesor():
    global profesores
    print(" ____________________________________________________")
    print("|                                                    |")
    print("|                Actualizar Profesor                 |")
    print("|____________________________________________________|")
    print()
    if len(profesores) == 0:
        print("No hay profesores registrados.")
    else:
        leer_profesores()
        codigo = input("Ingrese el código del profesor a actualizar: ")
        for profesor in profesores:
            if profesor["codigo"] == codigo:
                nombre = input("Ingrese el nuevo nombre del profesor: ")
                curso = input("Ingrese el nuevo curso del profesor: ")
                profesion = input("Ingrese la nueva profesión del profesor: ")
                profesor["nombre"] = nombre
                profesor["curso"] = curso
                profesor["profesion"] = profesion
                print("Profesor actualizado con éxito.")
                break
        else:
            print("No se encontró un profesor con ese código.")

def eliminar_profesor():
    global profesores
    print(" ____________________________________________________")
    print("|                                                    |")
    print("|                   Eliminar Profesor                |")
    print("|____________________________________________________|")
    print()
    if len(profesores) == 0:
        print("No hay profesores registrados.")
    else:
        leer_profesores()
        codigo = input("Ingrese el código del profesor a eliminar: ")
        for profesor in profesores:
            if profesor["codigo"] == codigo:
                profesores.remove(profesor)
                print("Profesor eliminado con éxito.")
                break
        else:
            print("No se encontró un profesor con ese código.")

        if len(profesores) == 0:
            print("No hay profesores registrados.")

def crud_estudiantes():
    while True:
        print(" ____________________________________________________")
        print("|                                                    |")
        print("|                CRUD de Estudiantes                 |")
        print("|____________________________________________________|")
        print("|1. Crear Estudiante                                 |")
        print("|2. Leer Estudiantes                                 |")
        print("|3. Actualizar Estudiante                            |")
        print("|4. Eliminar Estudiante                              |")
        print("|5. Salir al menú principal                          |")
        print("|____________________________________________________|")
        print()
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            crear_estudiante()
        elif opcion == "2":
            leer_estudiantes()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intente nuevamente.")

def crear_estudiante():
    global estudiantes
    print(" ____________________________________________________")
    print("|                                                    |")
    print("|                 Crear Estudiante                   |")
    print("|____________________________________________________|")
    print()
    nombre = input("Ingrese el nombre del estudiante: ")
    curso = input("Ingrese el curso del estudiante: ")
    carnet = input("Ingrese el carnet del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
    estudiante = Estudiante(nombre, curso, carnet, carrera)
    estudiantes.append(estudiante.__dict__)
    print("Estudiante creado con éxito.")
    print()

def leer_estudiantes():
    global estudiantes
    print(" ____________________________________________________")
    print("|                                                    |")
    print("|                   Estudiantes                      |")
    print("|____________________________________________________|")
    print()
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for estudiante in estudiantes:
            json_string = f'''{{
    "nombre": "{estudiante["nombre"]}",
    "curso": "{estudiante["curso"]}",
    "carnet": "{estudiante["carnet"]}",
    "carrera": "{estudiante["carrera"]}"
}}'''
            print(json_string)

def actualizar_estudiante():
    global estudiantes
    print(" ____________________________________________________")
    print("|                                                    |")
    print("|                Actualizar Estudiante               |")
    print("|____________________________________________________|")
    print()
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        leer_estudiantes()
        carnet = input("Ingrese el carnet del estudiante a actualizar: ")
        for estudiante in estudiantes:
            if estudiante["carnet"] == carnet:
                nombre = input("Ingrese el nuevo nombre del estudiante: ")
                curso = input("Ingrese el nuevo curso del estudiante: ")
                carrera = input("Ingrese la nueva carrera del estudiante: ")
                estudiante["nombre"] = nombre
                estudiante["curso"] = curso
                estudiante["carrera"] = carrera
                print("Estudiante actualizado con éxito.")
                break
        else:
            print("No se encontró un estudiante con ese carnet.")

def eliminar_estudiante():
    global estudiantes
    print(" ____________________________________________________")
    print("|                                                    |")
    print("|                 Eliminar Estudiante                |")
    print("|____________________________________________________|")
    print()
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        leer_estudiantes()
        carnet = input("Ingrese el carnet del estudiante a eliminar: ")
        for estudiante in estudiantes:
            if estudiante["carnet"] == carnet:
                estudiantes.remove(estudiante)
                print("Estudiante eliminado con éxito.")
                break
        else:
            print("No se encontró un estudiante con ese carnet.")

        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")

def main():
    menu()

if __name__ == "__main__":
    main()
