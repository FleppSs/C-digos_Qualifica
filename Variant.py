# = é associação
n1 = int(input("Insert a number: "))
n2 = int(input("Insert other number: "))
soma = n1 + n2
n3 = int(input("Insert a number: "))
n4 = int(input("Insert other number: "))
subtracao = n3 - n4
print("Resultado da soma é: {} e a subtracao é: {} ".format(soma, subtracao))
# .format poupa o trabalho de colocar o resultado da soma e subtracao usando {}, também é possivel colocar a ordem: {0}
print(type(n1))  # o type serve para verificar tipe de variavel
Read_Something = input("Input something: ")
print("The primitive type of this valor is: ", type(Read_Something))
print("Only have spaces?", Read_Something.isspace())
print("It´s a number?", Read_Something.isnumeric())
print("It´s alphabetical?", Read_Something.isalpha())
print("It´s alphanumerical?", Read_Something.isidentifier())
print("It´s alphabetical?"), Read_Something.isalnum()
print("It´s in uppercase?", Read_Something.isupper())
print("It´s in lowercase?", Read_Something.islower())
print("The first one is in uppercase?", Read_Something.istitle())
print("It´s with decimal numbers?", Read_Something.isdecimal())
