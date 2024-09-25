# Escreva um prorama para aprovar um empréstimo bancário para a compra de uma casa.. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal. Sabendo que ela
# não pode exceder 30% do salário ou então um empréstimo será negado. Exemplo: uma caasa custa 200 000 e seu salário é
# 3 000 e quero pagar a casa em 50 anos
Casa = float(input("Digite o valor da casa: R$"))
Salario = float(input("Digite quanto você ganha por mês: R$"))
Anos = int(input("Digite quantos anos deseja pagar o empréstimo: "))
mes = Anos * 12
prestacao = Casa / mes
limit = Salario * 0.30
if prestacao <= limit:
    print(f"Você vai pagar R${prestacao:.2f} por mês.")
else:
    print("O empréstimo não foi aprovado")