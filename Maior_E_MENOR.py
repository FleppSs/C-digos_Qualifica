# Crie um programa que leia 3 números inteiros e diga qual é o maior e menor
num1 = int(input("Digite um número "))
num2 = int(input("Digite outro número "))
num3 = int(input("Digite ouro número "))
if num1 > num2 > num3:
    print(f"O maior número é {num1} e o menor é  {num3}")
elif num3 > num1 > num2:
    print(f"O maior  número é {num3} e o menor é {num2}")
elif num2 > num3 > num1:
    print(f"O maior número é {num2} e o menor é {num1}")
elif num1 > num3 > num2:
    print(f"O maior número é {num1} e o menor é {num2}")
elif num2 > num1 > num3:
    print(f"O maior número é {num2} e o menor é {num3}")
elif num3 > num2 > num1:
    print(f"O maior número é {num3} e o menor é {num1}")