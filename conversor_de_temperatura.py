# crie um programa que convertar uma temperatura digitada em graus Celsius e Converta em Fahrenheit
C = float(input("Digite quantos graus celsius para converter em fahrenheit: "))
F = C * 1.8 + 32
print("{} graus convertidos para fahrenheit dá {}".format(C, F))