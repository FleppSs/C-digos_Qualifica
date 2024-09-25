# num = 1
# resposta = "S"
# # while num != 0:
# somar = 0
# while resposta == "S":
#     num += int(input("Digite um valor: "))
#     resposta = input("Deseja continuar? (S/N): ").upper()
#     somar += num
#     print(num)


# MOVIMENTAÇÃO DA RECEPÇÃO
# crie um programa que conte o número de pessoas que passaram pela recepção a partir
# das 7 da manhã até 20h. o programa deve exibir uma mensagem indicando que a contagem começou as 7 da manhã.
# Na primeira vez que o usuário digitar a hora inteira o programa verifica se é menor que 7 horas enquanto ele for,
# mostra uma mensagem de hora inválida e pede novamente. Durante o funcionamento, o programa pede ao usuário
# a quantidade de pessoas que passaram.
# Se for um horário maior que 20 horas o  programa encerra e mostra o total de pessoas que passaram o dia inteiro.
from datetime import datetime

agora = datetime.now().hour
pessoas = 0
hora_de_inicio = 7
hora_do_fim = 20
total = 0
if agora < 7:
    print(f"Não estamos aberto!! Abrimos somente ás 7!! Horário atual: {agora}")
elif agora > 20:
    print(f"Passamos do horário de funcionamento! Volte amanhã. Hora atual: {agora}")
else:

    while agora >= hora_de_inicio and agora <= hora_do_fim:
        pessoas = int(input(f"Hora atual: {agora} \n Quantas pessoas entraram?: "))
        total += pessoas
        agora += 1
        if agora > 20:
            break

print(f"Horário de funcionamento encerrado. No total, {total} pessoas entraram. Das 7 até às 20.")
