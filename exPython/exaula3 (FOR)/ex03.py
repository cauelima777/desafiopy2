
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


print("Conversão de Temperatura de Fahrenheit para Celsius:")
print("Fahrenheit \t Celsius")


for fahrenheit in range(50, 151, 10):
    celsius = fahrenheit_para_celsius(fahrenheit)
    print("{:9} \t {:7.2f}".format(fahrenheit, celsius))
