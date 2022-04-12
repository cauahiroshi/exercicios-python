#Cauã Hiroshi Dias Tamari T1

import modulo_semana

dia = int(input('Digite um dia entre 1 e 7: '))

while dia >7 or dia <1:
    print('Valor invalido! Digite um numero entre 1 e 7')
    dia = int(input('Digite o dia: '))
    
modulo_semana.dia_da_semana(dia)
