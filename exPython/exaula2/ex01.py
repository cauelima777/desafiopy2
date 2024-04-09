print("Digite as 4 notas")
resp1 = float(input()) 
resp2 = float(input()) 
resp3 = float(input()) 
resp4 = float(input()) 

media = (resp1 + resp2 + resp3 + resp4) / 4

if media >= 7.0 and media < 10.0: 
    print("Aprovado!")
    print(media)
elif media == 10.0:  
    print("Aprovado com distinção!")
    print(media)
else: 
    print("Reprovado! ")
    print(media)
