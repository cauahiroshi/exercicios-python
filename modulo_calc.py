# Cauã Hiroshi Dias Tamari T1

def somar(x, y, z):
    resultado = x + y + z
    print('A soma dos numeros é', resultado)

def menu_valores():
    x = float((input('Digite um valor numerico para x: ')))
    y = float((input('Digite um valor numerico para y: ')))
    z = float((input('Digite um valor numerico para z: ')))

    somar(x, y, z)

menu_valores()