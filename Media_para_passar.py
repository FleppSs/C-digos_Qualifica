
prova1 = float(input("Digite a nota da sua primeira prova: "))
media = 8.0
falta = (media * 2) - prova1
if falta <= 10:
    print(f"Você está na média. Pontos restantes para ser aprovado: {falta}! Continue como bom trabalho")
if falta > 10:
    print(f"TÚ É BURRO? CLARO QUE É. PRECISA TIRAR {falta} NA SEGUNDA PROVA PARA FICAR NA MÉDIA, OU SEJA, você não vai "
          f"conseguir.""")