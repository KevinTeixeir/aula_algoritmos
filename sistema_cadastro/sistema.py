# Lista de clientes usando um dicionário
clientes = {}

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
        clientes[email] = cliente
        print(f"cliente foi adicionado com sucesso, nome{clientes[email]}")

# Função para exibir todos os clientes
def exibir_clientes():
    if not clientes:
        print("nao possui clientes ainda")
    else:
        for email, cliente in clientes.items():
            print(f"nome: {cliente['nome']}, email: {cliente['email']}, telefone: {cliente['telefone']}, endereço: {cliente['endereco']}")

# Função para buscar cliente por email
def buscar_cliente(email):
    if email in clientes:
        cliente = clientes[email]
        print(f"Cliente encontrado: Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}, Endereço: {cliente['endereco']}")
    else:
        print("Cliente não encontrado")
# Função para remover cliente por email
def remover_cliente(email):
     if email in clientes:
        del clientes[email]
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
