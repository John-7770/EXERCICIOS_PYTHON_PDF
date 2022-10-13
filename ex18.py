paises = str(input('que pais voce gostaria de visitar: '))
cidade = str(input('que cidades voce gostaria de visitar: '))
idioma = str(input('que idioma voce gostaria de aprender: '))
celular = str(input('que celular voce gostaria de ter: '))
redes = str(input('que rede social è sua preferida?? '))
cor = str(input('qual cor voce gosta?? '))
lista = [paises, cidade, idioma, celular, redes]

print('\na ordem esta original!!!')
print(lista)

print('\na lista esta em ordem alfabetica')
print(sorted(lista))

print('\na lista esta original')
print(lista)

print('\na lista esta em ordem alfabetica reversa')
print(sorted(lista, reverse=True))

print('\na lista esta original')
print(lista)

print('\na lista esta toda ao reverso')
lista3 = lista
lista3.reverse()
print(lista3)

print('\na lista voltou ao normal')
lista4 = lista
lista4.reverse()
print(lista4)

print('\na lista esta em ordem alfabetica sem poder mudar!!!')
lista1 = lista
lista1.sort()
print(lista1)

print('\na lista vai ficar em ordem alfabetica reversa sem poder mudar')
lista2 = lista
lista2.sort(reverse=True)
print(lista2)
