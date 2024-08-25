#lista de clientes
clientes = []
name =""
email = ""
telefone = ""
endereco = ""
#função para adicionar clientes
def adicionar_clientes(name, email, telefone, endereco):
        print("-=-=-=-=-=-=-=-=-=--=-=")
        name = str(input("escreva seu nome: "))
        email = str(input("escreva seu email: "))
        telefone = str(input("escreva seu telefone: "))
        endereco = str(input("escreva seu endereço: "))
        clientes.append(name)
        clientes.append(email)
        clientes.append(telefone)
        clientes.append(endereco)
        return clientes

#função para exibir clientes
def exibir_clientes(clientes):
        if not clientes:
            print("-=-=-=-=-=-=-=-=-=--=-=")
            print("a lista não possui nenhum clinete ainda")    
        else:
            print(clientes)

#função para buscar clientes
def buscar_cliente():
        buscar = str(input("buscar email: "))
        for cliente in clientes:   
            if cliente == buscar:
                print(cliente)
                print("-=-=-=-=-=-=-=-=-=--=-=")
                break
        else: 
            print("email nao encontrado")

#função para remover clientes
def remover_cliente():
        rm_email = str(input("digite o email para q seja removido: "))
        for cliente in clientes:
            if cliente == rm_email:
                clientes.remove(cliente)
                print(clientes)
        else:
             print("cliente não foi encontrado")


#programa principal
#laço condicional do menu inical do programa
while True:
    print("-=-=-=-=-=-=-=-=-=--=-=")
    print("0. adicionar cliente")
    print("1. para remover email:")
    print("2. para buscar email")
    print("3. para ver lista completa")
    print("4. para parar o programa:")
    print()
    #entrada para escolher uma das opções abaixo
    choice = str(input("escolha uma das opções abaixo: "))
    if choice == "0":
          adicionar_clientes(name,email,telefone,endereco)
    elif choice == "1":
        remover_cliente()        
    elif choice == "2":
        buscar_cliente()
    elif choice == "3":
        exibir_clientes(clientes)
    elif choice == "4":
          break