# Crie um programa que leia o valor a ser economizado
# e a quantidade que voC~e guarda todo mês
# calcule a quantidade de meses para atingir a meta e exiba na tela
eco = float(input("Quanto você guarda todo mês?"))
val = float(input("Qual valor terá que ser atingido?: "))
mes = val / eco
print(f"A sua meta é R${val} e você pode economizar R${eco}. Precisaria de {mes:.0f} meses")