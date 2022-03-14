# Autor: Margarida Balola
# versão: 0.0.1
# data: 11/03/2022

#pedir dia da semana

diasem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

while True:
    valor = input('Introduzir o dia da semana')
    if valor != diasem:
        print('O valor introduzido não é valido')
        break
    elif valor == 'Sábado' or valor == 'Domingo':
        print('O dia da semana não é dia útil')
    else:
        print('O dia da semana é dia útil')

''' verificar se é dia útil ou não
if diasem == 'Sábado' or diasem == 'Domingo':
    print('O dia da semana não é dia útil')
else:
    print('O dia da semana é dia útil')'''