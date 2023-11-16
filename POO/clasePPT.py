"""Aqui se hace uso de dos formas de establecer una clase, sin constructor y con el constructor, empezamos a relacionar nuevos conceptos, como clase, atributos, init o constructor, self y metodos  """

# Definición de la clase Estudiante usando un método tradicional sin constructor

class Estudiante:
    # Atributos de la clase
    codigo = 0
    nombre = ""
    apellido = ""

    # Método para imprimir datos del estudiante
    def imprimir_Datos(self, codigo, nombre, apellido):
        print(self.codigo, self.nombre, self.apellido)

# Crear un objeto adso de la clase Estudiante
adso = Estudiante()

# Acceder a través del objeto adso a los atributos de la clase Estudiante y asignar valores
adso.codigo = 1
adso.nombre = 'Sandra'
adso.apellido = 'Cruz'

# Llamar al método imprimir_Datos para imprimir los datos del estudiante
adso.imprimir_Datos(adso.codigo, adso.nombre, adso.apellido)


# Definición de la clase Estudiante1 usando un constructor (__init__)

class Estudiante1:
    # Constructor de la clase que se llama al crear una instancia
    def __init__(self, codigo, nombre, apellido):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido

    # Método para imprimir información del estudiante
    def imprimir_Informacion(self):
        print(self.codigo, self.nombre, self.apellido)

# Crear un objeto adso1 de la clase Estudiante1 usando el constructor
adso1 = Estudiante1(2, 'Maria', 'Galindo')

# Llamar al método imprimir_Informacion para imprimir la información del estudiante
adso1.imprimir_Informacion()
