# Lista de clientes usando um dicionário
clientes = []

# Função para adicionar clientes
def adicionar_clientes(nome, email, telefone, endereco):
    if email in clientes:
        print("cliente ja foi cadastrado! ")
    
    else:
        cliente = {
            "nome": nome,
            "email":email,
            "telefone":telefone,
            "endereco":endereco,
        }
        clientes.append(cliente)
        print(f"cliente foi adicionado com sucesso. nome {nome}")
        return clientes
# Função para exibir todos os clientes
def exibir_clientes():
    if not clientes:
        print("nao possui clientes ainda")
    else:
        print(clientes)

# Função para buscar cliente por email
def buscar_cliente(email):
    for cliente in clientes:
        if cliente["email"] == email:
            print(f"Cliente encontrado: Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}, Endereço: {cliente['endereco']}")
        else:
            print("Cliente não encontrado")
# Função para remover cliente por email
def remover_cliente(email):
     
     for cliente in clientes:
        if cliente["email"] == email:
            clientes.remove(cliente)
            print("cliente removido")
        else:
            print("não foi possivel remover o cliente")

# Programa principal - Menu
def menu():
    while True:
        print("-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=")
        print("0. Adicionar cliente")
        print("1. Remover cliente por email")
        print("2. Buscar cliente por email")
        print("3. Ver lista completa de clientes")
        print("4. Parar o programa")
        print("-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=")
        
        # Entrada para escolher uma das opções
        escolha = input("Escolha uma das opções acima: ")

        if escolha == "0":
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            telefone = input("Digite seu telefone: ")
            endereco = input("Digite seu endereço: ")
            adicionar_clientes(nome, email, telefone, endereco)

        elif escolha == "1":
            email = input("Digite o email do cliente para remover: ")
            remover_cliente(email)

        elif escolha == "2":
            email = input("Digite o email do cliente para buscar: ")
            buscar_cliente(email)

        elif escolha == "3":
            exibir_clientes()

        elif escolha == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
