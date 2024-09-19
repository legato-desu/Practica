class Fabrica:
    def __init__(self, empresa, ubicacion, ingreso_anual):
        self.empresa = empresa
        self.ubicacion = ubicacion
        self.ingreso_anual = ingreso_anual
        
    def ver_atributos(self):
        print("\n\t🏭")
        print(f" \___{self.empresa}___/")
        print(f" - Ubicacion: {self.ubicacion}")
        print(f" - Ingreso anual: {self.ingreso_anual}")

fabrica_1 = Fabrica("Ducati ","Italia","€1.000 millones")
fabrica_2 = Fabrica("Harley Davidson ","Wisconsin","$4.888 millones")
fabrica_3 = Fabrica("Marine Turbine Technologies","Estados Unidos","$925.000")

fabrica_1.ver_atributos()
fabrica_2.ver_atributos()
fabrica_3.ver_atributos()