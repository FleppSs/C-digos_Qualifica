# Crie um programa que verifique se as palavras: Python, Criminoso, Cartão de Crédito< Mário estão na presentesw na
# na lista de palavras. Exiba a palavra em uma mensagem indicando se foi encontrada usando o FOR
Words = ["Python", "Criminoso", "Cartão de crédito", "Mario"]
other_words = ["Java Script", "Kahoot", "Mario", "Python", "Programação"]
for pal in Words:
    if pal in other_words:
        print(f"A palavra \033[32:35m{pal}\033[m foi encontrada na lista")
    else:
        print(f"A palavra \033[0:30:41m{pal}\033[m dentro da variavél não foi encontrada na lista")