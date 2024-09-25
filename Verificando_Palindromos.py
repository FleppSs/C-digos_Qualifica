# Escreva um programa que verifique se a palavra ou frase digitada é um palindromo
Text = input("Digite o texto: ").upper().replace(" ", "")
rev = Text[::-1]

if Text == rev:
    print("Sua palavrra é um palíndromo.")
else:
    print("Sua palavra não é um palindromo")