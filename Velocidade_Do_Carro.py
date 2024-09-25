# Crie um programa que leia a velocidade de um carro se ele ultrapassar 80km/h
# diz que ele vai ser multado por 7 reais a cada valor acima do limite
import time
print("-----------------------------Radar Eletrônico-----------------------------")
vel = float(input("Digite a velocidade do seu carro: "))
mult = 7
multa = (vel - 80)
pay = multa * mult
print("Processando....")
time.sleep(2)
if vel > 80:
    print(f"Você excedeu {multa}km/h do limite de 80km/h. Terá de pagar R${pay} pela multa")
    print("--------------------------------------------------------------------------")
else:
    print("Você está dentro da velocidade limite.")
    print("--------------------------------------------------------------------------")
