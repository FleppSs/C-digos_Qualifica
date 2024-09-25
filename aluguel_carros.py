# Cria um programa que leia a quantidade de quilometros percorridos
# por um carro alugado e a quantidade e dias pelos quais ele foi alugado
# calcule o peço a pagar sabendo que o carro custa R$60,00 por dias a R$0,60 kilometros rodado
KM = float(input("Quantos KM seu carro alugado percorreu?"))
Day = float(input("Quantos dias seu carro foi alugado?"))
Km = 0.60 * KM
day = 60 * Day
pay = Km + day
print("Você percorreu KM{}, então terá que pagar R${:.2f} por KM rodados".format(KM, Km))
print(f"Você ficou {Day} dia(s) com o carro, então terá que pagar R${day} pelo aluguel.")
print(f"Ao todo vocÊ terá que pagar R${pay}")