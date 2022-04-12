#Cauã Hiroshi Dias Tamari T1

velocidade = int(input('Digite a velocidade do seu carro: '))

velocidade_maxima = 50
multa = (velocidade - velocidade_maxima) * 200 

if velocidade > velocidade_maxima:
    print('Você vai receber uma multa de R$', + multa)
    print('Ande mais devagar')
else:
    print('Você esta liberado')

