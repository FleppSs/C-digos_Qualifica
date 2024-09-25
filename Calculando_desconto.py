# Crie um programa que leia o preço de um produto
# e mostre seu novo preço com 5% de desconto
valor = float(input("Digite o preço de seu produto: "))
percentual = float(input("Quantos % de desconto você quer? "))
dis = valor * (percentual / 100)
fin = valor - dis
print("O valor do produto é R${}, com disconto de {}%, o valor passa para R${:.2f}".format(valor, percentual, fin))