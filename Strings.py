phrase = "Im Murilo Ribeiro"
print(phrase[0:18:2])  # da 0 até 18 de 2 em 2
print(phrase[:4])  # só vai até a 4 que na verdade é a anterior
print(phrase[3:])  # começa depois da 3
print(phrase[3::3])
print(len(phrase))
print(phrase.count("o"))
print(print(phrase.count("i", 0, 12)))
print(phrase.find("Ribei"))
print(phrase.find("Jomurgandr"))  # quando não existe, o resultado é sempre -1
print("Muri" in phrase)
# perguntando se existe "Muri" na string
print(phrase.replace("Murilo", "FleppS"))  # troca uma pela outra
print(phrase.upper())
print(phrase.lower())
print(phrase.capitalize())  # capitalize torna só a primeira letra em
print(phrase.title())
phrase2 = "  Learning in Qualifica   "
print(phrase2.strip())
print(phrase2)
print(phrase2.rstrip())
print(phrase2.lstrip())
print(phrase2.split())
print(" - ".join(phrase2))
print("".join(phrase2))
print("""Python é amplamente utilizado devido à sua simplicidade e versatilidade. É empregado em desenvolvimento web,
ciência de dados, inteligência artificial e automação  de tarefas.
Empresas e desenvolvedores  escolhem o Python por sua vasta biblioteca de módulos e comunidade ativa. Além disso, a 
linguagem permite uma rápida prototipagem e desenvolvimento eficiente de projetos complexos.""")
print(len(phrase2), phrase2.upper().count("i"))
print(len(phrase2.upper()))
computer_description = "Esse é um computador que foi lançado e chegou para revolucionar o mercado"
print(computer_description[5])  # para trazer o último caractere, o - inverte a contagem
print(computer_description.index("o"))
print(computer_description[2:-4])

name = "Murilo"
sub = "Ribeiro"
print("Nome: ", name, sub)
test = input("Alterar seu nome: ")
test2 = input("Alterar sobrenome: ")
test3 = test + test2
resposta = test, test2
print("Nome alterado: ", resposta)
