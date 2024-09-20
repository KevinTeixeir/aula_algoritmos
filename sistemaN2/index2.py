
# Gerenciamento de Tarefas Simples

# Função para adicionar uma nova tarefa
def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    novo_id = len(lista_tarefas) + 1  # Novo ID baseado no tamanho da lista
    tarefa = {"Id": novo_id, "descricao": descricao, "status": status, "prioridade": prioridade}
    lista_tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada!\n")

# Função para visualizar todas as tarefas
def visualizar_tarefas(lista_tarefas):
    if not lista_tarefas:
             print("nao possui tarefas ainda")
    else:
        for tarefa in lista_tarefas:
            print("todas as tarefas:")
            print(f"id {tarefa["Id"]}, descrição {tarefa["descricao"]}, status {tarefa["status"]}, prioridade {tarefa["prioridade"]}")
        

# Função para filtrar tarefas por status e/ou prioridade
def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    tarefas_filtradas = [tarefa for tarefa in lista_tarefas 
                         if (status is None or tarefa["status"] == status) and 
                            (prioridade is None or tarefa["prioridade"] == prioridade)]
    return tarefas_filtradas

# Exemplo de uso

lista_tarefas = []

# Adicionando tarefas
adicionar_tarefa(lista_tarefas, "Implementar login", "pendente", "alta")
adicionar_tarefa(lista_tarefas, "Escrever documentação", "em andamento", "média")
adicionar_tarefa(lista_tarefas, "desenvolver modelagem", "em andamento", "baixa")
adicionar_tarefa(lista_tarefas, "desenvolver front-end", "pendente", "alta")
    
# Visualizando todas as tarefas
print("Todas as tarefas:")
visualizar_tarefas(lista_tarefas)

# Filtrando por status e prioridade
print("Tarefas pendentes:")
visualizar_tarefas(filtrar_tarefas(lista_tarefas, status="pendente"))

print("Tarefas com prioridade alta:")
visualizar_tarefas(filtrar_tarefas(lista_tarefas, prioridade="alta"))
