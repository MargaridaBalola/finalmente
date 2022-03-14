diasem = input('Introduzir dia da semana')

if diasem in ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'):
    print('O dia da semana é dia útil')
elif diasem in ('Sábado', 'Domingo'):
    print('O dia da semana não é dia útil')
else:
    print('O dia não é valido')