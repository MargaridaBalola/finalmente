# Autor: Margarida Balola
# versão: 0.0.1
# data: 11/03/2022

#identificação da palavra passe
passw = 'Passe_certa'
numero = 1

while numero <= 3:
    numero = numero + 1
    passe = input('Introduzir a palavra passe')
    if passw == passe:
        print("Enhorabuena")
        break
    '''else:
        print("Passe Errada")'''