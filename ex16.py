print('pense 5 cidades que voce gostaria de visitar no mundo'.title())
cg = str(input('1 cidade: '))
cg1 = str(input('2 cidade: '))
c2 = str(input('3 cidade: '))
c3 = str(input('4 cidade: '))
c4 = str(input('5 cidade: '))

lista = [cg, cg1, c2, c3, c4,]
print('\nlista original')
print(lista)

print('\na lista foi modificada pra aparecer em ordem alfabetica')
print(sorted(lista))

print('\na lista esta original')
print(lista)

print('\nnessa lista ela foi ordenada reversa')
print(sorted(lista, reverse=True))

print('\na lista nao ocorreu alteraçoes')
print(lista)

print('\na lista foi alterada para mudar a ordem e ficar reversa')
lista1 = lista
lista1.reverse()
print(lista1)

print('\na lista voltou ao normal')
lista6 = lista
lista6.reverse()
print(lista6)

print('\na mudou pra ficar em ordem alfabetica')
lista2 = lista
lista2.sort()
print(lista2)

print('\na lista vai ficar em ordem alfabetica reversa')
lista3 = lista
lista.sort(reverse=True)
print(lista3)