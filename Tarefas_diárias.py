lista_de_tarefas = ["LAVAR LOUÇA", "LIMPAR A CASA", "ESTUDAR", "PYTHON", "FAZER EXERCICIOS", "BEBER AGUA"]
print(f"LISTA DE TAREFAS A SEREM FEITAS: {lista_de_tarefas}")
while True:
    feito = str(input("Digite a tarefa feita: ").upper())
    if feito == "LAVAR LOUÇA":
        lista_de_tarefas.remove("LAVAR LOUÇA")

    if feito == "LIMPAR A CASA":
        lista_de_tarefas.remove("LIMPAR A CASA")

    elif feito == "ESTUDAR":
        lista_de_tarefas.remove("ESTUDAR")

    elif feito == "PYTHON":
        lista_de_tarefas.remove("PYTHON")

    elif feito == "FAZER EXERCICIOS":
        lista_de_tarefas.remove("FAZER EXERCICIOS")

    elif feito == "BEBER AGUA":
        lista_de_tarefas.remove("BEBER AGUA")
    print("---------------LISTA DE TAREFAS---------------")
    print(lista_de_tarefas)
    if len(lista_de_tarefas) == 0:
        print("Todas as tarefas foram feitas")
        break
