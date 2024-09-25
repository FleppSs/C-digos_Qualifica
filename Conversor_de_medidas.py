# Conversor de medidas
# crie um programa que leia um valor em metros
# e exiba os valores em centimentros e milimetros
metros = int(input("Insira uma quantidade de metros pra converter: "))
centi = metros / 100 * 10000
mili = centi / 100 * 1000
print("A quantidade de {}m para centimetros fica {}cm, e para milimetros é {}mm".format(metros, centi, mili))
