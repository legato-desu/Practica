# Ejercicio 101
import areas, volumenes
"""
Cree 3 modulos:
1 - principal.py donde va el main con un procedimiento titulo que imprima "Ejemplo de modulos"
2- areas.py cree 3 funciones para: Circulo, Triangulo y Rombo
3 - volumenes.py cree 3 funciones para: Circunferencia, Cono y Cilindro

Importe en areas.py principal.py, que imprime?
"""
def principal():
    print("Ejemplo de modulos")

if __name__ == "__main__":
    principal()
    
    # areas.py
    print(f"Área del círculo 'radio = 4':\n{areas.circulo(4):.2f} cm²")
    print(f"Área del triángulo 'base = 4, altura = 8':\n{areas.triangulo(4, 8):.0f} cm²")
    print(f"Área del rombo 'diagonal mayor = 8, diagonal menor = 4':\n{areas.rombo(8, 4):.0f} metros²")

"""
    # volumenes.py
    print(f"Circunferencia = 5:\n{volumenes.circunferencia(5):.4f} cm")
    print(f"Cono 'radio = 3, altura = 7':\n{volumenes.cono(3, 7):.2f} cm³")
    print(f"Cilindro 'radio = 4, altura = 10':\n{volumenes.cilindro(4, 10):.2f} m³ ")
"""