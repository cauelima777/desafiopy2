import math

print("Digite os valores das variáveis da equação ax^2 + bx + c")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existem raízes reais")

elif delta == 0:
    x = -b / (2*a)
    print("Resultado da equação:", x)

else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Resultado da equação:","x1 =", x1, "e","x2 =", x2)
