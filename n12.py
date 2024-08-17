def contV(p):
    vogais = "aeiouAEIOU"
    CONTAvogais = 0
    for letras in p:
        if letras in vogais:
            CONTAvogais +=1
    print(CONTAvogais)

palvra = input(str())
contV(palvra)