# 5 + 2 == soma
# 5 - 2 == subtração
# 5 * 2 == multiplicação
# 5 ** 2 == potencia
# 5 // 2 == divisão ao inteiro
# 5 % 2 == resto da divisão
# 5 / 2 == divisão
# == comparação

print("a soma de 5 e 2 é: ", 5 + 2)
print("A subtração de 5 e 2 é: ", 5 - 2)
print("A divisão de 5 e 2 é: ", 5 * 2)
print("5 levado ao quadrado dá o resultado de: ", 5 ** 2)
print("A divisão ao inteiro de 5 e 2 é: ", 5 // 2)
print("O resto da divisão entre 5 e 2 é: ", 5 % 2)
print("O resultado da divisão entre 5 e 2 é: ", 5 / 2)

# () Tuplas
# [] Listas
# {} Dicionário
# a maior prioridade de calculo é o parenteses ()
# a segunda maior prioridade de cálculo é a potencia **
# terceira maior prioridade de cálculo é a /,*,//,% ambas tem a mesma prioridade só que a ordem é da primeira a última.
# as últimas prioridades de cálculo são + e -

print(pow(25, 3))  # pow ou "power" serve para potencias
print(81 ** (1/2))  # elevando a potencia de meio serve para calcular a raiz quadrada = [Um número] ** (1/2)
print("oi" + "olá")  # o + adiciona a segunda string à primeira {Ocorre uma junção} ou {Concatenar-Concatenação}
print("oi", "olá")
print("Prof " * 5)  # Esse comando repete a string o número de vezes pedido. Coloque espaço ou então estará tudo junto
print("DINHEIRO " * 99)
print("=" * 99)
print("1 =" * 20)
name = input("Qual é o seu nome sua criatura? ").title()
# Eu atribui a varivel name a um input ou declarei a variavel

print("Que desgosto em te conhecer {:20}!".format(name))
print("Desgosto inenarravél em te conhecer {:>20}!!!".format(name))  # Jogou o nome para a direita dando 20 espaços
print("Desgosto inenarravél em te conhecer {:^20}!!!".format(name))  # O ^ centraliza {10} à esquerda e 10 à direita}
print("Desgosto inenarravél em te conhecer {:-^20}!!!".format(name))  # Coloca # no lugar dos espaços ou o que você quer

n1 = int(input("Qual o primeiro valor? "))
n2 = int(input("Qual o segundo valor? "))
print("A soma desses valores é {}".format(n1 + n2))
# o input só retorna informações em forma de string então se coloca o INT para ele entender como um valor númerico

soma = n1 + n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
expo = n1 ** n2
print("A soma é {},\nO produto é {:.2f},\n A divisão é {:.2f};".format(soma, mult, div), end="")
print("\nA divisão inteira é {:.2f},\n E poência é {:.2f}.".format(div_int, expo))
# :.2f signfica que eu quero só duas casas decimais após a virgula,ou seja, limitando. [f] = [Float]