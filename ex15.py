print      ('\nquem voce quer adicionar para o jantar? '.title())

c = str(input('\n escolha 1 pessoa: '))
c1 = str(input('\n escolha mais 1 pessoa: '))
c2 = str(input('\n escolha mais 1 pessoa: '))

lista = []
lista.append(c)
lista.append(c1)
print(50*'')
lista.append(c2)
print(50*'=')
print('{} voce quer ir jantar em casa hoje?'.title().format(lista[0]))
print('quero sim obrigado pelo convite.'.title())
print(50*'=')
print('{} voce quer ir jantar em casa hoje?'.title().format(lista[1]))
print(' vou ver qualquer coisa te ligo convite !!!')
print(50*'=')
print('{} voce quer ir jantar em casa hoje?'.title().format(lista[2]))
print('quero sim obrigado pelo convite a noite apareço la !!!')
print('me desculpe mais nao poder ao jantar !!!')
print(50*'=')
print('\ne agora ??? convide outra pessoa ')
c2 = str(input('convide outra pessoa:'))
lista[2] = c2
print(50*'=')
print('\t\n{} como uma pessoa nao pode ir ao meu jantar voce pode ir ??'.format(lista[2]))
print('\tre:nao posso garantir que vou brinks vou sim economizar comida ')
print('\tvoce>obrigado {} '.format(lista[2]))
print('\tconvidado > de nada  ')
print(50*'=')
print('parece que tem uma mesa maior ali na frente  vamos convidar mais pessoas ')
print('\nconvide mais amigos!!!')

c3 = str(input('\n convide um amigo:' ))
c4 = str(input('\n convide mais amigo: '))
c5 = str(input('\n convide mais um  amigo: '))

lista.append(c3)
lista.append(c4)
lista.append(c5)

print(50*'=')
print('\tola {} gostaria de ir a um jantar ?? '.format(lista[3]))
print('ola  claro que horas sao ?? e starei la !!')
print('20:00')
print(50*'=')
print('\tola {} gostaria de ir  um jantar ?? '.format(lista[4]))
print('ola estou livre esta noite mesmo vou sim que horas sao??')
print('20:00')
print(50*'=')
print(' \tola {} gostaria de ir a um jantar?? '.format(lista[5]))
print('vou sim estou de folga hoje trampo foi foda mais vou assim ')
print('obrigado, estou feliz por todos irem jantar comigo!!!'.title())
print(50*'=')
print                 ('estou grato por todos terem vindo '.upper())
print(50*'=')
print('a mesa nao chegou a tempo entao eu vou ter convidar apenas um !!!')
removidos = lista.pop(5)
removidos = lista.pop(4)
removidos = lista.pop(3)
removidos = lista.pop(2)
print('como disse agora so tem lugares entao so vou poder convidar apenas dois \ne esses  sao {} E {} \n desculpem todos'.format(lista[0], lista[1]))
del lista[1]
del lista[0]