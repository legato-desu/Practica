class Moto:
    def __init__(self, marca, uso, cilindrada):
        self.marca = marca
        self.uso = uso
        self.cilindrada = cilindrada
        
    def ver_atributos(self):
        print("\n\t🏍️")
        print(f" \___{self.marca}___/")
        print(f" - Uso: {self.uso}")
        print(f" - Cilindrada: {self.cilindrada:,}cc")

moto_1 = Moto("Yamaha ","Carreras",1000)
moto_2 = Moto("Suzuki ","Urbano",600)
moto_3 = Moto("kawasaki","Touring",1400)

moto_1.ver_atributos()
moto_2.ver_atributos()
moto_3.ver_atributos()