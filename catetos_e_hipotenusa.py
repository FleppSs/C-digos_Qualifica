# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o cumprimento da hipotenusa
import math
op = float(input("Digite o comprimento do cateto oposto: ")) ** 2
adj = float(input("Digite o comprimento do cateto adjacente: ")) ** 2
hip = (op + adj) ** (1/2)
print(f"O comprimento da hipotenusa é {hip:.0f}")
