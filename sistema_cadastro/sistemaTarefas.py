tarefas = []

def adicionar_tarefas(lista_tarefas, descricao, status, prioridade):
    novo_id = len(tarefas) + 1
    lista_tarefas={
        "id": novo_id,
        "descricao": descricao,
        "status" : status,
        "prioridade":prioridade,
    }
    tarefas.append(lista_tarefas)
    print(f"tarefa foi adicionada. descrição: {descricao} ")
    return tarefas

def visualizar_tarefas(lista_tarefas):
        for tarefass in lista_tarefas:
              print(f"id: {tarefass['id']}, descrição: {tarefass['descricao']}, status: {tarefass['status']}, prioridades: {tarefass['prioridade']} ")
#def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):

adicionar_tarefas("fazer botao", "criar um botao azul", "pendente", "alta")
adicionar_tarefas("fazer nav", "criar um nav azul", "pendente", "alta")
adicionar_tarefas("fazer nav", "criar ul", "pendente", "alta")
adicionar_tarefas("fazer nav", "crm nav azul", "pendente", "alta")
visualizar_tarefas(tarefas)