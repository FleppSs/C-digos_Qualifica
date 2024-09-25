# crie um programa que pergunte a distância da viagem em km, calcule o  preço da passagem cobrando. R$2 a cada km
# de viafem até 200km e R$1,50 para viagens ,mais longas acima de 200km
import time
print("-------------------Custo da viagem-------------------")
Km = float(input("Digite quantos KM você vai percorrer nessa viagem: "))
Km2 = Km * 2
Km1 = Km * 1.50
print("Calculando custo...")
time.sleep(2)
if Km <= 200:
    print(f"Você pagará R${Km2} pela viagem.")
elif Km > 200.001:
    print(f"Você pagará R${Km1} pela viagem")