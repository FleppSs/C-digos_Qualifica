# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre a sua categoria de acordo com a idade:
# Até 9 anos - Mirim
# até 14 anos - Infantil
# Até 19 anos - Junior
# Até 25 anos - Sênior
# Acima de 25 anos - Master
from datetime import date
ano = int(input("Digite o ano em que você nasceu: "))
ano_atual = date.today().year
idade = ano_atual - ano
if idade < 9:
    print("Você é um atleta da categoria mirim.")
elif 9 <= idade < 14:
    print("Você é  um atleta da categoria infantil.")
elif 14 <= idade < 19:
    print("Você é um atleta da categoria junior.")
elif 19 <= idade < 25:
    print("Você é um atleta da categoria sênior.")
elif 25 <= idade:
    print("Você é um atleta da categoria master.")