
def tabla_multiplicar(numero):
    for i in range(10):
        print(f"{ i + 1 } * { numero } = { numero * (i + 1)}")

def area_circulo(radio):
    print(f"El área de un circulo de radio { radio } es { 3.14 * radio ** 2 } cm2")

def run():
    print("Se imprime la tabla de ultiplicar del 16\n")
    tabla_multiplicar(16)

    print("Calcula un radio 24cm")
    area_circulo(24)


if __name__ == '__main__':
    run()