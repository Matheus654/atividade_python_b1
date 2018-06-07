x = input("Escolha a operação: A = adição, S = subtração, D = divisão ou M = multiplicação: ")
n1 = int(input("digite um número: "))
n2 = int(input("digite outro número: "))
if x == "A":
    print(n1 + n2)
if x == "S":
    print(n1 - n2)
if x == "M":
    print(n1 * n2)
if x == "D":
    if n2 != 0:
        print(n1 / n2)
    if n2 == 0:
        print("Error")
