import random

nomes = ["Sayori", "Zelda", "Monika", "Sally", "Asgore", "Jojo", "James", "Makoto"]
nome_escolhido = random.choice(random.sample(nomes, 8)).upper()
acerto = ['_'] * len(nome_escolhido)
erro = []
tentativas = 10


while tentativas > 0:
    print(''.join(acerto))
    print(f"[{tentativas}] Tentativas restantes")
    print(f"Letras erradas: {erro}")
    escolha = input("Digite a letra que você quer escolher: ").upper()
    if escolha in acerto or escolha in erro:
        print("Você já escolheu essa!")
    if escolha in nome_escolhido:
        for tem in range(len(nome_escolhido)):
            if nome_escolhido[tem] == escolha:
                acerto[tem] = escolha
    else:
        erro.append(escolha)
        tentativas -= 1
    if '_' not in acerto:
        print(f"VOCÊ VENCEU!!! O NOME ERA {nome_escolhido}")
        break
    if tentativas == 0:
        print(f"Você perdeu! O nome era: {nome_escolhido}")
        break
