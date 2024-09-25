preco = float(input("Digite o valor do produto: "))
print("----------------OPÇÕES DE PAGAMENTO----------------")
print("(1) A vista no dinheiro, com 10% de desconto.")
print("(2) A vista no cartão, com 5% de desconto.")
print("(3) Em 2 vezes no cartão com o preço normal.")
print("(4) Em 3 vezes ou mais no cartão com 35% de juros.")
op = int(input("Digite a opção de pagamento: "))
if op == 1:
    des = preco * 0.90
    print(f"O valor final será R${des}")
elif op == 2:
    des = preco * 0.95
    print(f"O valor final será R${des}")
elif op == 3:
    print(f"O valor final é R${preco}")
elif op == 4:
    des = preco * 1.35
    print(f"O valor final será R${des}")
else:
    print("Opção inválida.")
