print      ('\nquem voce quer adicionar para o jantar? '.title())
c = str(input('\nquem voce quer convidar para o jantar? '))
c1 = str(input('\nescolha mais 1 pessoa: '))
c2 = str(input('\nescolha mais 1 pessoa: '))
lista = []
lista.append(c)
lista.append(c1)
print(50*'')
lista.append(c2)
print('{} voce quer ir jantar em casa hoje?'.title().format(lista[0]))
print('quero sim obrigado pelo convite.'.title())
print(40*'')
print('{} voce quer ir jantar em casa hoje?'.title().format(lista[1]))
print(' vou ver qualquer coisa te ligo convite !!!')
print(50*'')
print('{} voce quer ir jantar em casa hoje?'.title().format(lista[2]))
print('quero sim obrigado pelo convite a noite apareço la !!!')
print('me desculpe mais nao poder ao jantar !!!')
print(50*'=')
print('\ne agora ??? convide outra pessoa ')
c2 = str(input('convide outra pessoa:'))
lista[2] = c2 
print(50*'')
print('\t{} como uma pessoa nao pode ir ao meu jantar voce pode ir ??'.format(lista[2]))
print('nao posso garantir que vou brinks vou sim economizar comida ')
print('obrigado {} '.format(lista[2]))
print('de nada  ')





