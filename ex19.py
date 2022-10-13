print('pense em 4 pizzas que voce gosta!!!')
pi = str(input('1 pizza: '))
pi2 = str(input('2 pizza: '))
pi3 = str(input('3 pizza: '))
pi4 = str(input('4 pizza: '))
pizzas = [pi, pi2, pi3, pi4]
print(pizzas)

for pizza1 in pizzas:
    print("\ngosto de pizza de " + pizza1.title())
    print("realmente adoro pizza de " + pizza1.upper() + " ela tem um sabor irresistivel" )