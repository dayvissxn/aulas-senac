import math
'''sistema calcule a area e o perimetro de um circulo'''
'''usuario insira o raio do circulo'''
raio = 0


def f_c_a():
    raio = float(input("Entre com o valor do raio: "))
    area = 3.14 * (raio * raio)
    print(f"Se o raio é: {raio:.2f}. A área é: {area:.2f}")

def f_c_p():
    raio = float(input("Entre com o valor do raio: ")) 
    perimetro = 2 * 3.14 * raio
    print(f"Se o raio é: {raio:.2f}. O perimetro é: {perimetro:.2f}")

def menu():
    while True:
        print("\n1. Área do circulo")
        print("2. Perimetro do circulo")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            f_c_a()
        elif escolha == '2':
            f_c_p()
        elif escolha == '3':
            print("Até logo!")
            return
        else:
            print("Opção inválida!")

menu()
        

