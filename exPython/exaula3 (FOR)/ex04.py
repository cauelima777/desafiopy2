
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


while True:

    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))


    print("\nMenu de Operações:")
    print("1. Somar os dois números")
    print("2. Subtrair o segundo número do primeiro")
    print("3. Multiplicar os dois números")
    print("4. Digitar novos números")
    print("5. Sair")


    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        print("Resultado da soma:", somar(num1, num2))
    elif escolha == 2:
        print("Resultado da subtração:", subtrair(num1, num2))
    elif escolha == 3:
        print("Resultado da multiplicação:", multiplicar(num1, num2))
    elif escolha == 4:
        continue  
    elif escolha == 5:
        print("Saindo do programa...")
        break  
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
