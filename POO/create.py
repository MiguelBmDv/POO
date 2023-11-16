# Clase base: Personaje
class Personaje:
    def __init__(self, nombre, nivel, puntos_vida):
        # Constructor de la clase base que inicializa atributos comunes a todos los personajes.
        self.nombre = nombre
        self.nivel = nivel
        self.puntos_vida = puntos_vida

    def atacar(self):
        # Método común para todos los personajes que representa un ataque genérico.
        return f"{self.nombre} realiza un ataque."


# Subclases: Guerrero y Mago
class Guerrero(Personaje):
    def __init__(self, nombre, nivel, puntos_vida, arma):
        # Constructor de la subclase Guerrero que llama al constructor de la clase base y añade atributos específicos.
        super().__init__(nombre, nivel, puntos_vida)
        self.arma = arma

    def atacar(self):
        # Método de ataque específico para la subclase Guerrero.
        return f"{self.nombre} ataca con {self.arma}."

class Mago(Personaje):
    def __init__(self, nombre, nivel, puntos_vida, hechizo):
        # Constructor de la subclase Mago que llama al constructor de la clase base y añade atributos específicos.
        super().__init__(nombre, nivel, puntos_vida)
        self.hechizo = hechizo

    def atacar(self):
        # Método de ataque específico para la subclase Mago.
        return f"{self.nombre} lanza el hechizo {self.hechizo}."


# Uso del polimorfismo
guerrero = Guerrero("Conan", 5, 100, "Espada")
mago = Mago("Gandalf", 7, 80, "Bola de Fuego")

# Mostrar información
print(f"{guerrero.nombre} - Nivel: {guerrero.nivel} - Puntos de Vida: {guerrero.puntos_vida}")
print(f"{mago.nombre} - Nivel: {mago.nivel} - Puntos de Vida: {mago.puntos_vida}")

# Realizar ataques
print(guerrero.atacar())  # Salida: Conan ataca con Espada.
print(mago.atacar())      # Salida: Gandalf lanza el hechizo Bola de Fuego.
