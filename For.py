# print("Qualifica")
# print("Qualifica")
# print("Qualifica")
# print("Qualifica")
# print("Qualifica")
# for contador in range(0, 5):
   # print("Qualifica")
   # print("Fim do programa")
# for contador in range(6, 0, -1): # o -1 imprime em ordem inversa
   # print("Qualifica")
   # print("Fim do programa")
# num = int(input("Digite um número de repetições: "))
# for contador in range(num, 0, -1):
#     print(contador)
# print("FIM")
#
# num_inicial = int(input("Digite o número iinicial: "))
# num_final = int(input("Digite o número final: "))
# pulos = int(input("Digite de quantos em quantos pulos de números ele vai fazeer: "))
#
# if pulos == 0:
#     print("Você é otário?")
#
# else:
#     for contador in range(num_inicial, num_final, pulos):
#         n = input("Digite um número: ")
#        # print(contador)
num_inicial = int(input("Digite o número inicial: "))
num_final = int(input("Digite o número final: "))
pulos = int(input("Digite de quantos em quantos irá pular: "))
if pulos == 0:
    print("Você é imbecil?")

somar = 0
for contador in range(num_inicial, num_final, pulos):
    n = int(input("Digite o número: "))
    somar = somar + n

print(f"O somatório desses números é {somar}")
print("-----------------------------------------------------------")
print("--------------------PROGRAMA FINALIZADO--------------------")
print("-----------------------------------------------------------")
