class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.resistencia = fuerza ** 2
        self.turno = False
        
    def ver_atributos(self):
        print(f"\n*** {self.nombre} *** ")
        print(f" - Fuerza: {self.fuerza}")
        print(f" - Inteligencia: {self.inteligencia}")
        print(f" - Defensa: {self.defensa}")
        print(f" - Vida: {self.vida}")
        print(f" - Resistencia: {self.resistencia}")
        print(f" - Turno: {self.turno}")

personaje_1 = Personaje("Caballero",6,7,9,3)
personaje_2 = Personaje("Princesa",1,10,2,5)
personaje_3 = Personaje("Heroe",10,10,10,"∞")
personaje_4 = Personaje("Villano", 10,10,5,10)

personaje_1.ver_atributos()
personaje_2.ver_atributos()
personaje_3.ver_atributos()
personaje_4.ver_atributos()