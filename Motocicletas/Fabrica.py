class Fabrica:
    def __init__(self, empresa, ubicacion, precio):
        self.empresa = empresa
        self.ubicacion = ubicacion
        self.precio = precio
        
    def ver_atributos(self):
        print("\n \___Fabrica___/")
        print("\t 🏭")
        print(f" - Fabrica: {self.empresa}")
        print(f" - Ubicacion: {self.ubicacion}")
        print(f" - Precio: ${self.precio:,}")

fabrica_1 = Fabrica("Yamaha ","Shizuoka",120000000)
fabrica_2 = Fabrica("Suzuki","Iwata-shi",12999000)
fabrica_3 = Fabrica("Kawasaki","Kobe",79000000)

fabrica_1.ver_atributos()
fabrica_2.ver_atributos()
fabrica_3.ver_atributos()