import time

init = time.time()
clientes = []

def adicionar_clientes(nome, email, telefone, endereco):
        clientes.append(nome)
        clientes.append(email)
        clientes.append(telefone)
        clientes.append(endereco)
        return clientes

def exibir_clientes(clientes):
        print(clientes)

def buscar_cliente(email):
        buscar = str(input("buscar email: ")).lower()
        if email == buscar:
            print(email)
            print("-=-=-=-=-=-=-=-=-=--=-=")
        else: 
            print("email nao encontrado")
def remover_cliente(email):
        clientes.remove(email)
        print(clientes)

print("-=-=-=-=-=-=-=-=-=--=-=")
nome = str(input("escreva seu nome: "))
email = str(input("escreva seu email: "))
telefone = str(input("escreva seu telefone: "))
endereco = str(input("escreva seu endereço: "))

while True:
    print("-=-=-=-=-=-=-=-=-=--=-=")
    print("0. adicionar cliente")
    print("1. para remover email:")
    print("2. para buscar email")
    print("3. para ver lista completa")
    print("4. para parar o programa:")
    print()
    escolha = str(input("escolha uma das opções abaixo: "))
    if escolha == "0":
          adicionar_clientes(nome,email,telefone,endereco)
    elif escolha == "1":
        remover_cliente(email)        
    elif escolha == "2":
        buscar_cliente(email)
    elif escolha == "3":
        exibir_clientes(clientes)
    elif escolha == "4":
          break
fim = time.time()
print(fim)