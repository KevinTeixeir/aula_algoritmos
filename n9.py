def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))
if primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
