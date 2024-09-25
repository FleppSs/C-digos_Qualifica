# crie um programa que pergunte o salário de um fucnionário e calcule o valor de seu aumento
# para salários superiores à R$1420 calculam um aumento de 10% para os inferiores ou iguais o aumento é de 15%
sal = float(input("Digite o valor do seu salário: R$"))
if sal > 1420.01:
    reajuste = sal * 1.10
    print(f"Seu novo salário será {reajuste:.2f}")
elif sal <= 1420:
    reajuste = sal * 1.15
    print(f"Seu novo salário será R${reajuste:.2f}")