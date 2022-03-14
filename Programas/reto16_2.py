# Autor: Margarida Balola
# versão: 0.0.1
# data: 11/03/2022

#opções dos dias da semna:
diasem = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")

#pedir dia da semana
valor = input('Introduzir o dia da semana')

#verificação do tipo de dia

if valor == 'Sábado' or valor == 'Domingo':
    print('O dia da semana não é dia útil')
elif valor in diasem:
    print('O dia da semana é dia útil')
else:
    print('O valor introduzido não é valido')
