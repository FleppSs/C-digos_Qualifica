# Crie um programa que conte quantas vogais (A, E, I, O, U) existem em uma frase fornecida pelo usuário.
import unicodedata
frase = str(input("Digite uma frase: ").upper())
frase_normal = unicodedata.normalize('NFKD', frase)
fraseSacento = " ".join(c for c in frase_normal if not unicodedata.combining(c))
vogais_count = 0
vogais = ["A", "E", "I", "O", "U",]
for letter in fraseSacento:
    if letter in vogais:
        vogais_count = vogais_count + 1
        print(F"Na frase temos \033[34m{vogais_count}\033[m vogais")
