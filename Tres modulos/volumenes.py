import math

def circunferencia(radio):
    return 2 * math.pi * radio

def cono(radio, h):
    return (1/3) * math.pi * radio**2 * h

def cilindro(radio,h):
    return math.pi * radio ** 2 * h