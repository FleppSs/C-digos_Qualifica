# Crie um programa qualquer e mostre se ele é bissexto ou não.
ano = int(input("Digite o ano para verificar se ele é bissexto: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Seu ano é bissexto")
else:
    print("Seu ano não é bissexto.")