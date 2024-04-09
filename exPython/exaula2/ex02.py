
print("Digite três valores numéricos:")
valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
valor3 = float(input("Valor 3: "))


maior = valor1
if valor2 > maior:
    maior = valor2
if valor3 > maior:
    maior = valor3


menor = valor1
if valor2 < menor:
    menor = valor2
if valor3 < menor:
    menor = valor3


print("O maior valor é:", maior)
print("O menor valor é:", menor)
