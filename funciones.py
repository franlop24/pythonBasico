
def tabla_multiplicar(numero):
    for i in range(10):
        print(f"{ i + 1 } * { numero } = { numero * (i + 1)}")

def area_circulo(radio):
    print(f"El área de un circulo de radio { radio } es { 3.14 * radio ** 2 } cm2")

def area_cuadrado(lado):
    print(f"El área de un cuadrado de lado { lado } es { lado * lado } cm2")

def peri_circulo(radio):
    print(f"El perimetro del circulo de radio {radio} es { 3.14 * (2 * radio) }")

def run():

    print("Calcula un lado 24cm\n")
    area_cuadrado(100)


if __name__ == '__main__':
    run()
