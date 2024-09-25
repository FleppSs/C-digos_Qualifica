


# def mostralinha():
#     print("=" * 21)
#     # print("SISTEMA".center(11))
#     # print("===========")
# mostralinha()
# print("Professor Alexandre".center(21))
# mostralinha()
# print(" ")
# mostralinha()
# print("Qualifica Maricá".center(21))
# mostralinha()




# def mensagem(msg):
#     print("=" * 40)
#     print(msg.center(40))
#     print("=" * 40)
#     print(" ")
#
# mensagem("Jogo do tigrinho")
# mensagem("RENDA EXTRA")



def mensagem(msg):
    ajustada = len(msg) + 6
    print("#" * ajustada)
    print(msg.center(ajustada))
    print("#" * ajustada)
    print(" ")


mensagem("Olá")