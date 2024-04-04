

def cadastro():
    print("CADASTRO")
    while True:
        try:
            nomec = str(input("Informe o seu Nome: "))
            cpfc = int(input("Informe o seu CPF: "))
            senhac = int(input("Informe a sua senha: "))
            break
        except ValueError:
            print("Para CPF e Senha saõ permitidos somente numeros!")
    cadastro = []
    cadastro.append (nomec)
    cadastro.append (cpfc)
    cadastro.append (senhac)
    print(cadastro)

cadastro()

'''
def login():
    print("SISTEMA DE LOGIN")
    while True:
        try:
            cpfl = int(input("Digite o seu login: "))
            senhal = int(input("Digite a sua senha: "))
        except ValueError:
            print("Para Login e Senha saõ permitidos somente numeros!")

def menu():
    print("SISTEMA")
    while True:
        print("Escolha a opção:")
        print("1 - Cadastro")
        print("2 - Login")
        opcao = input("Opção: ")

        if opcao == '1':
            cadastro()
        elif opcao == '2':
            login()
            break
        else:
            print("Opção Inválida: ")
menu()'''