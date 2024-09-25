# Crie um programa que receba uma lista de palavras e exiba as pallavras que tem mais de 5 caracteres
lista = ["Python", "Java", "C", "JavaScrypt", "HTML", "GoLang"]
for cara in lista:
    if len(cara) > 5:
        print(f"A palavra \033[32m{cara}\033[m tem mais de 5 caracteres")