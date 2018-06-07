x = int(input("indique um número: "))
y = int(input("indique outro número: "))
z = int(input("indique outro número"))
if x + y > z and x + z > y and z + y > x:
    print("Esses valores admitem um triângulo")
    if x == y == z:
        print("E esse triângulo é equilátero")
    elif x == y != z or x == z != y or z == y != x:
        print("E esse triângulo é isósceles")
    elif x != y != z:
        print("E esse triângulo é escaleno")
else:
    print("Esses valores não admitem um triângulo")
