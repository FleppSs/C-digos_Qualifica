# Crie um programa que conte o número  de palavras em uma frase fornecida pelo usuário
###################### JEITO 01 ######################
phrase = input("Digite uma frase: ").split()
print(f"A frase contém {len(phrase)} palavras")


################### JEITO 02 #########################

phrase = input("Digite uma frase: ").split()
contador = 0

for palavra in phrase:
    contador += 1 # contador = contador + 1
print(f"A sua frase contém {len(phrase)} palavras")