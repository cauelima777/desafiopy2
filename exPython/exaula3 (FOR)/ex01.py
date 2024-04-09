
def calcular_fatorial(numero):

    if numero == 0:
        return 1
    else:
    
        fatorial = 1
       
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

numero = int(input("Digite um número inteiro maior que zero: "))\


if numero > 0:

    resultado = calcular_fatorial(numero)

    print("O fatorial de {} é {}.".format(numero, resultado))
else:
    print("O número inserido não é maior que zero.")


