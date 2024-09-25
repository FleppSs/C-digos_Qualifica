# Calculando IMC
# Crie um programa que leia o peso e a altura do usuário
# Calcule o IMC e depois exiba na tela
altura = float(input("Digite sua alura em metros: "))
peso = float(input("Digite seu peso em KG: "))
IMC = peso / (altura ** 2)
if 16 > IMC:
    print("TÁ PASSANDO FOME?????? TEU IMC É {}, VAI COMER!!!".format(IMC))
elif 16.1 <= IMC < 16.9:
    print("Seu IMC é de {}, cuidado com ventos leves!!!!".format(IMC))
elif 17 <= IMC < 18.4:
    print("Teu IMC é de {}, você é um pouco magro mas tá ok".format(IMC))
elif 18.5 <= IMC < 24.9:
    print("Seu IMC é de {}, peso na média.".format(IMC))
elif 25 <= IMC < 29.9:
    print("Cara, teu IMC é {}... Tá um pouco gordo.".format(IMC))
elif 30 <= IMC < 34.9:
    print(f"SEU OBESO MORBIDO TIPO 1, TEU IMC É DE {IMC}!! PROCURA FAZER UMA DIETA E FAZER EXERCICIOS")
elif 35 <= IMC < 39.9:
    print(f"Então amigo(a) se você não fechar essa sua boca... O que vai fechar vai ser sua vida. Seu IMC é {IMC}.")
elif 40 < IMC:
    print(f"""Tú tá pior que a Thais Carla!!! CUIDE-SE OU VAI AFUNDAR O PLANETA COM SEUS PASSOS
    SEU BALÃO, CAIXA D'AGUA, BALEIA, RINOCERONTE, ROLHA DE CRATERA!! IMC de {IMC}""")