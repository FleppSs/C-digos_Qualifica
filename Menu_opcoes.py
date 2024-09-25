# crie um pograma que leia dois números e mostre um menu de opcoes:
# 1 pra somar
# 2 pra multiplicar
# 3 maior valor
# 4 novos números
# o programa deverá realizar a operação solicitada em cada acesso

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

while True:

    soma = num1 + num2
    mult = num1 * num2
    print("-----------------Opções-----------------")
    print("[1] Somar [2] Multiplicar [3] Maior valor [4] Novos números [5] Sair")
    opcoes = int(input())
    if opcoes == 1:
        print(f"O valor da soma é: {soma}")
    elif opcoes == 2:
        print(f"O valor da multiplicação é: {mult}")
    elif opcoes == 3:
        if num1 > num2:
            print(f"O maior valor é {num1}")
        elif num1 == num2:
            print("Ambos os valores são iguais.")
        else:
            print(f"O maior valor é {num2}")
    elif opcoes == 4:
        num1 = 0
        num2 = 0
        num1 += float(input("Digite o primeiro valor: "))
        num2 += float(input("Digite o segundo valor: "))
    elif opcoes == 5:
        break
print("Programa finalizado.")