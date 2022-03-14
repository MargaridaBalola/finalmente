# Autor: Margarida Balola
# versão: 0.0.1
# data: 11/03/2022

#nome da aplicação CalculadoraInversa

# Definição dos numeros e sinal
num1 = int(input('Introduzir valor1'))
num2 = int(input('Introduzir valor2'))
sinal = input('Introduzir sinal')

#calculos
soma = num1 + num2
resta = num1 - num2
multp = num1 * num2
div = num1 / num2
exp = num1 ** num2
mod = num1 % num2

if sinal == '+':
    print(('A soma dos valores é: '), soma)
elif sinal == '-':
    print(('A subtração dos valores é: '), resta)
elif sinal == '*':
    print(('A multiplicação dos valores é: '), multp)
elif sinal == '/':
    print(('A divisão dos valores é: '), div)
elif sinal == '**':
    print(('A subtração dos valores é: '), exp)
elif sinal == '%':
    print(('A subtração dos valores é: '), mod)
else:
    print('O valor do sinal não é válido')


from tkinter import *
from tkinter import messagebox
app = Tk()
app.title("CalculadoraInversa")
app.geometry("500x300")

messagebox.showinfo(title="CalculadoraInversa", message = "O resultado final é")