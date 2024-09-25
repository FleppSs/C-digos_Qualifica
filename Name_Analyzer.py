# Desafio: Analisador de texto
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas e minusculas
# Quantas letras ao todo sem considerar os espaços
# Quantas letras tem o primeiro nome.
Insira = input("Insira seu nome: ").strip()
InsiraS = input("Insira seu sobrenome: ").strip()
Nome = Insira + " " + InsiraS
print("Seu nome é: ", Insira)
print("Seu sobrenome é: ", InsiraS)
print("Seu nome maiusculo ficaria: ", Nome.upper())
print("Seu nome minusculo ficaria: ", Nome.lower())
print("Quantidade de digitos no seu nome é: ", len(Insira + InsiraS))
print("Agora só o primeiro nome é: ", len(Insira))
