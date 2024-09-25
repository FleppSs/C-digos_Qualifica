# crie um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade se ele ainda
# vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento o programa
# também deverá mostrar o tempo que fala ou o que já passou do prazo também.
from datetime import date
print("----------------------ALISTAMENTO_MILITAR_ONLINE---------------------")
day = int(input("Digite o dia em que você nasceu: "))
month = int(input("Digite o mês em que você nasceu: "))
nasc = int(input("Digite o ano em que você nasceu: "))
year = 2024 - nasc
if year > 18:
    atr = year - 18
    print(f"Você está {atr} ano(s) atrasado para se alistar.")
elif year == 18:
    print("Você pode se alistar.")
elif year < 18:
    res = 18 - year
    print(f"Falta {res} ano(s) para você poder se alistar.")
ano_atual = date.today().year
idade = ano_atual - nasc
print(f"Quem nasceu em {nasc} tem {idade} em {ano_atual}")