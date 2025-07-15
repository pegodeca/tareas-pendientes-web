FILEPATH = "tareas.txt"

# En este bloque se comienza la definición de funciones

def leer_todos(filepath=FILEPATH):
    """ Lee el contenido de un archivo de texo 
        y lo añade a una lista
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def guardar_todos(todos_arg, filepath=FILEPATH):
    """ Escribe en un fichero de texto, una lista de tareas pendientes,
        que tenemos en una lista
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# Final del bloque de definición de funciones

if __name__ == "__main__":
    print("Saludos desde funcinoes")
