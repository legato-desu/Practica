class Moto:
    def __init__(self, modelo, uso, cilindrada):
        self.modelo = modelo
        self.uso = uso
        self.cilindrada = cilindrada
        
    def ver_atributos(self):
        print("\n \___Motocicleta___/")
        print("\t 🏍️")
        print(f" - Modelo: {self.modelo}")
        print(f" - Uso: {self.uso}")
        print(f" - Cilindrada: {self.cilindrada:,}cm³")

moto_1 = Moto("YZF-R1M ","Carreras",998)
moto_2 = Moto("Gixxer","Urbano",250)
moto_3 = Moto("GTR","Touring",1352)

moto_1.ver_atributos()
moto_2.ver_atributos()
moto_3.ver_atributos()