# faça um programa que leia quanto dinheiro uma pessoa tem
# mostre e diga quantos dólares uma pessoa pode comprar
# considere 1 dollar US$1,00 = R$4,8
din = float(input("Digite quanto você tem em reais na conta bancária: "))
dollar = din / 4.8
euro = din / 6.0
print("Você tem a quantidade de R${} e pode comprar a quantia de US${:.2f}".format(din, dollar))
print("Você também pode comprar €{} euros.".format(euro))
