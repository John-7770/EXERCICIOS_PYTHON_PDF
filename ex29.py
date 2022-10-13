print('pense em 4 pizzas que voce gosta!!!')
pi = str(input('1 pizza: '))
pi2 = str(input('2 pizza: '))
pi3 = str(input('3 pizza: '))
pi4 = str(input('4 pizza: '))
pizzas = [pi, pi2, pi3, pi4]
friend_pizzas = pizzas[:]
print("\nexistem 2 listas")
pizzas.append('quatro queijo')
friend_pizzas.append('brigadeiro')
print(pizzas)

print(friend_pizzas)
print("\nminhas pizzas favoritas sao:")
for pizzaS in pizzas:
    print(pizzaS)
print("\nas pizzas favoritas do meu amigo sao:")
for Pizzas in friend_pizzas:
    print(Pizzas)