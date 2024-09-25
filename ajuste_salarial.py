# crie um programa que leia o salário de um funcionário e moste seu novo salário com 16% de aumento
sal = float(input("Digite a quantia do seu salário: R$"))
ajuste = float(input("Digite a porcentagem de ajuste: "))
mud = sal * (ajuste / 100)
fin = sal + mud
print("Você recebia R${} e agora vai receber R${:.2f}".format(sal, fin))