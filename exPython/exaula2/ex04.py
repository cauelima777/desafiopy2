print("=======Menu de operações======")
print("1.           -Somar             ")
print("2.           -Subtrair          ")
print("3.           -Multiplicar       ")
print("==============================")
resp = float(input())


if resp == 1: 
    print("Escolha 2 valores para somar")
    a = int(input())
    b = int(input())

    soma = a + b
    
    print("Resultado da soma: ", soma)

elif resp == 2: 
    print("Escolha 2 valores para subtrair")
    a = int(input())
    b = int(input())
    subtracao = a - b 
    print("Resultado da subtração: ", subtracao)

elif resp == 3: 
    print("Escolha 2 valores para multiplicar")
    a = int(input())
    b = int(input())
    multiplicacao = a*b

else: 
    print("ERROR")
