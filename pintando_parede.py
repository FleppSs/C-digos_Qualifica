# crie um programa que leia a largura e a altura de uma parede em metros
# calcule sua área, e a quantidade necessária de tinta para pintar
# sabendo que cada litro  de tinta pinta uma área de 2 metros quadrados
largura = float(input("Digite o a lagura de sua parede: "))
altura = float(input("Digite a altura de sua parede: "))
area = largura * altura
print("-------------------------------------------------------------------------------------------------")
print("""Sua parede tem {}m de altura, {}m de largura 
e uma área de {} metros quadrados""".format(altura, largura, area))
tinta = area / 2
print("Para pintar sua parede seria necessário a quantidade de {} litros de tinta".format(tinta))
print("-------------------------------------------------------------------------------------------------")
