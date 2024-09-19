class Piloto:
    def __init__(self, edad, categoria, peso):
        self.edad = edad
        self.categoria = categoria
        self.peso = peso
        
    def ver_atributos(self):
        print("\n\t 😎")
        print(f" - Edad: {self.edad} años")
        print(f" - Categoria: {self.categoria}")
        print(f" - Peso: {self.peso} kg")

piloto_1= Piloto(20,"MotoGP",65)
piloto_2= Piloto(55,"Chopper",90)
piloto_3 = Piloto(7,"Motocross Infantil",37)

piloto_1.ver_atributos()
piloto_2.ver_atributos()
piloto_3.ver_atributos()