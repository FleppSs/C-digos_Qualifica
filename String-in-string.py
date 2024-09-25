frase = str(input("Escreva sua frase a seguir para analisar as letras A do texto: ").lower())
print("Sua frase é: ", frase)
print("Analisando, aguarde um segundo...")
print("ANÁLISE COMPLETA")
print("-------------------------------------------------------------------------")
print("Resultados: ")
print("Sua frase tem a quantidade de {} A. ".format(frase.count("a")))
digito = "O primeiro a está no digito de número {}."
print(digito.format(frase.find("a")+1))
digito3 = "E o último a está no digito de número {}."
print(digito3.format(frase.rfind("a")+1))
# O pokemon abra pode ser facilmente encontrado no inicio do jogo e sua última evolução só esá disponivel por troca.
print("-------------------------------------------------------------------------")
