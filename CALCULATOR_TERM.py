  def add(a,b):
    return a+b
def remove(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b == 0:
        print("Operatie inutila")
        return a
    else:
        return a/b

def print_partial(value):
    print("Rezultat partial: ", value)

operatie = 0
total = float(input())
while operatie != "=":
    operatie = input()
    if operatie != "=":
        alt_numar = float(input())

    if operatie == "+":
        total = add(total, alt_numar)
        print_partial(total)

    elif operatie == "-":
        total = remove(total, alt_numar)
        print_partial(total)
    elif operatie == "*":
        total = multiply(total, alt_numar)
        print_partial(total)
    elif operatie == "/":
        total = division(total, alt_numar)
        print_partial(total)

    else:
        print("Rezultat final: ", total)
        print(["programul s-a incheiat"])


