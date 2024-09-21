
def buscaSequencial(lista, chave):
    n = len(lista)
    for índice in range(n):        
        if lista[índice] == chave:
            return índice
    return -1

chave = 45
lista = [20, 5, 15, 24, 67, 45, 1, 76, 21, 11]

pos = buscaSequencial(lista, chave)
if pos != -1:
    print("Posição da chave", chave, "na lista:", pos)
else:
    print("A chave", chave, "não se encontra na lista")
# Posição da chave 45 na lista: 5