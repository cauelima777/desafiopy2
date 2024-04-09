print("Digite um número maior que zero para o fatorial")
fatorial = int(input()) # 3

resultado = 1


if fatorial > 0:

    while fatorial > 1:
        resultado *= fatorial # 1 * 3 = 3//
        fatorial -= 1  # 3 - 1 = 2//


    print("O fatorial é:", resultado)
else:
    print("O número fornecido não é maior que zero.")
