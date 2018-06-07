x = int(input("digite um número: "))
y = int(input("digite outro número: "))
z = int(input("digite mais um número: "))
if x > y > z:
    print('em ordem decrescente',x,y,z,'e em ordem crescente',z,y,x)
if x > z > y:
    print('em ordem decrescente',x,z,y,'e em ordem crescente',y,z,x)
if y > x > z:
    print('em ordem decrescente',y,x,z,'e em ordem crescente',z,x,y)
if y > z > x:
    print('em ordem decrescente',y,z,x,'e em ordem crescente',x,z,y)
if z > x > y:
    print('em ordem decrescente',z,x,y,'e em ordem crescente',y,x,z)
if z > y > x:
    print('em ordem decrescente',z,y,x,'e em ordem crescente',x,y,z)
