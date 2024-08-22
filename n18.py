import random
import time

ini = time.time()
moeda = random.randint(1,2)
if moeda == 1:
    print("cara")
else:
    print("coroa")
exec = time.time()
print(exec)
