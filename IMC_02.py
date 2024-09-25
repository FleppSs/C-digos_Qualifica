# crie um programa que leia o peso e altura de alguém e calcule seu IMC e mostre seus status de acordo com seu IMC
# abaixo de 18,
altura = float(input("Digite sua alura em metros: "))
peso = float(input("Digite seu peso em KG: "))
IMC = peso / (altura ** 2)
if 18.5 > IMC:
    print("Teu imc é {}, está abaixo do peso.".format(IMC))
elif 18.5 <= IMC < 25:
    print("Seu IMC é de {}, está no peso ideal.".format(IMC))
elif 25 <= IMC < 30:
    print("Teu IMC é de {}, sobrepeso.".format(IMC))
elif 30 <= IMC < 40:
    print("Seu IMC é de {}, obesidade.".format(IMC))
elif 40 <= IMC:
    print("teu IMC é {}... Obesidade mórbida.".format(IMC))
