def soma(a,b):
    return print(a + b)
def sub(a,b):
    return print(a - b)
def mult(a,b):
    return print(a * b)
def div(a,b):
    return print(a / b)


op = input("qual operação deseja realizar? + , - , * , /")

n1 = int(input("n1: "))
n2 = int(input("n2: "))

if op == "+":
    res = soma(n1, n2)
elif op == "-":
    res = sub(n1, n2)
elif op == "*":
    res = mult(n1, n2)
elif op == "/":
    res = div(n1, n2)
    