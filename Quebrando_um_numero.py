# crie um programa que leia um número real qualquer e mostre na tela
# sua porção inteira.
# Exemplo: se eu digitar 6.789 ele vai pegar o  valor 6
import math
num = float(input("Digite seu número:"))
print("O número real é {}".format(num.__floor__()))
