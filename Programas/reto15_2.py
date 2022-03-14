# Autor: Margarida Balola
# versão: 0.0.1
# data: 11/03/2022

# numero de vendas a introduzir
numven = int(input('Introduzir número de vendas'))

soma = 0
numero = 1
# introduzir o valor de cada venda
while numero <= numven:
    numero = numero + 1
    valor = int(input('Introduzir valor da venda', numven))
    soma = soma + valor


print('A soma das vendas é', soma)