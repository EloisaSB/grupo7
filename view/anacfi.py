class Personaje:
    def __init__(self, nombre, salud, poder=5):
        self.nombre = nombre
        self.salud = salud
        self.poder = poder

    def atacar(self):
      return self.poder


class Mago(Personaje):
    def __init__(self, nombre, salud, poder_magico):
        super().__init__(nombre, salud)
        self.poder_magico = poder_magico

    def atacar(self):
        ataque = self.poder_magico * self.poder  # Aquí debes usar "self.poder_magico" y "self.poder"
        print(f"{self.nombre} lanza un hechizo con poder {ataque}")


class Guerrero(Personaje):
    def __init__(self, nombre, salud, fuerza):
        super().__init__(nombre, salud)
        self.fuerza = fuerza

    def atacar(self):
        ataque = self.fuerza * self.poder  # Aquí debes usar "self.poder_magico" y "self.poder"
        print(f"{self.nombre} lanza un hechizo con poder {ataque}")

# Crear objetos de las clases hijas
mago1 = Mago(
  "Merlín", #NOMBRE
  100,      #VIDA
  50        #PODER_MAGICO
  )

guerrero1 = Guerrero(
  "Conan",  #NOMBRE
  150,      #VIDA
  80        #FUERZA
  )

# Polimorfismo: Tratar a los objetos como objetos de la clase padre
personajes = [mago1, guerrero1]

for personaje in personajes:
    personaje.atacar()
