
pessoas = []

while True:
    nome = input("Digite o nome da pessoa ou 'fim' para encerrar: ")
    

    if nome.lower() == 'fim':
        break
    
    idade = int(input("Digite a idade de {}: ".format(nome)))
    

    pessoas.append((nome, idade))

if pessoas:

    pessoa_mais_velha = pessoas[0]
    
    # Percorre a lista de pessoas para encontrar a mais velha
for pessoa in pessoas:
    if pessoa[1] > pessoa_mais_velha[1]:
            pessoa_mais_velha = pessoa
    
    # Imprime o nome e a idade da pessoa mais velha
    print("A pessoa mais velha é {} com {} anos.".format(pessoa_mais_velha[0], pessoa_mais_velha[1]))
else:
    print("Nenhuma pessoa foi inserida.")
