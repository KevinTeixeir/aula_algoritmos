cadastro = {}
#função q vai armazenar o valor
def cadastrar(nome, email):
    cliente = {
        "nome": nome,
        "email":email
    }

    cadastro[email] = cliente
    print(f"cliente {cadastro[email]}, foi cadastrado!") 

def exibir(email):
    if not email in cadastro:
        print("ainda nao possui cadastro")
    else:
        for email, cliente in cadastro.items():
            print(f"nome: {cliente['nome']}, email: {cliente['email']}") 

#recebe um valor que é armazenado em dicionario
while True:
    
    print("0 para cadastrar: ")
    print("1 para exibir: ")
    print("2 para parar o programa: ")

    escolha = str(input("digite o q deseja fazer: "))

    if escolha == "0":
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        cadastrar(nome, email)
    elif escolha == "1":
        email = str(input("dighite seu email para exibir seu cadastro!"))
        exibir(email)
    elif cadastrar == "2":
        break
    else:
        print("tente novamente")
