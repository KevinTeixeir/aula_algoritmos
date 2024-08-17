import random


maquina = random.randint(1,5)
print(" escolha um numero, se for o msm que a maquina esta pensando voce ganha")
usuario = int(input(""))

if usuario == maquina:
    print("parabens vc ganhou")
else:
    print("voce perdeu")
