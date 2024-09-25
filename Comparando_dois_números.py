# crie um pograma que leia dois números inteiros e compare-os mostrando a mensagem na tela
# o primeiro valor maior o segundo valor maior
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
if num2 > num1:
    print(f"O maior número é {num2} e o segundo maior é {num1}")
elif num2 == num1:
    print("Os valores são iguais.")
else:
    print(f"O maior número é {num1} e o segundo maior é {num2}")