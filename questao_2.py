x = float(input("digite seu salário: "))
if x <= 280.00:
    print('seu salário antes do reajuste era',x,)
    print('então você receberá um aumento de 20%')
    print('você terá um aumento de',x * 0.2,)
    print('seu salário agora será,', x + x * 0.2)
elif (x > 280.00 and x <= 700.00):
    print('seu salário antes do reajuste era',x,)
    print('então você receberá um aumento de 15%')
    print('você terá um aumento de',x * 0.15,)
    print('seu salário agora será', x + x * 0.15,)
elif x > 700.00 and x <= 1500.00:
    print('seu salário antes do reajuste era',x, )
    print('então você receberá um aumento de 10%')
    print('você terá um aumento de', x * 0.1, )
    print('seu salário agora será,', x + x * 0.1)
elif x > 1500.00:
    print('seu salário antes do reajuste era', x, )
    print('então você receberá um aumento de 5%')
    print('você terá um aumento de', x * 0.05,)
    print('seu salário agora será,', x + x * 0.05)
