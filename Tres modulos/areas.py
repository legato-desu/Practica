import math, principal

def circulo(radio):
    return math.pi * radio ** 2

def triangulo(a,h):
    return (a * h) / 2

def rombo(mayor,menor):
    return (mayor * menor)/2

if __name__ == "__main__":
    principal.principal()

"""
Al ejecutar este codigo "areas.py" teniendo su importacion "principal.py" se lanzara por pantalla
el mensaje contenido en el modulo "principal.py" dando asi por ejecucion "Ejemplo de modulos"
"""