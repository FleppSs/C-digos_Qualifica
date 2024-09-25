# Desafio: Calculadora do valor da hora e dia trabalhado
# Crie um programa que leia o salário mensal e a quantidade de horas trabalhadas por dia, depois calcule o valor da hora
# e do dia trabalhado ao final exibir  na tela os valores da hora e dia trabahados
sal = float(input("""Digite o valor do salário mensal:  
R$"""))
hour = int(input("Digite as horas que você trabalha por dia: "))
day = int(input("Quantos dias ao mês você trabalha?: "))
daysal = sal / day
hoursal = daysal / hour
print(f"Você recebe R${daysal:.2f} por dia e R${hoursal:.2f} por hora trabalhada.")