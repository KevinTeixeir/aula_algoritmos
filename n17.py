ntermos = 100

fibonacci = [0, 1]

for i in range(2, ntermos):
    proximoT = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximoT)


print(f"Os primeiros {ntermos} números da sequência de Fibonacci são:")
print(fibonacci)