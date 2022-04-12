#Cauã Hiroshi Dias Tamari T1

instalacao_r = 'Residencial'
instalacao_c = 'Comercial'
instalacao_i = 'Industrial'

print('Tipos de Instalação: Residencial, Comercial ou Industrial')
instalacao = input('Digite o tipo de instalação que voce deseja calcular: ')

while instalacao != instalacao_r and instalacao != instalacao_c and instalacao != instalacao_i:
      print('ERRO! Digite um tipo valido')
      instalacao = input('Digite o tipo de instalação que voce deseja calcular: ')

energia_consumida = float(input('Digite a quantidade de kWh consumida: '))

#calculando consumo de energia residencial
if instalacao == instalacao_r:
    print('\nCalculando consumo de energia Residencial\n')

    if energia_consumida < 500:
        preco = 0.45
    else:
        preco = 0.65
    
    valor_a_pagar= energia_consumida * preco
    print('Houve um consumo de', energia_consumida,'kWh de energia')
    print('A residencia vai ter que pagar R$', '%.2f' % valor_a_pagar,'de energia consumida')

#calculando consumo de energia comercial
elif instalacao == instalacao_c:
    print('\nCalculando consumo de energia Comercial\n')

    if energia_consumida < 1000:
        preco = 0.55
    else:
        preco = 0.60
    
    valor_a_pagar= energia_consumida * preco
    print('Houve um consumo de', energia_consumida,'kWh de energia')
    print('O comercio vai ter que pagar R$', '%.2f' % valor_a_pagar,'de energia consumida')

#calculando consumo de energia industrial
elif instalacao == instalacao_i:
    print('\nCalculando consumo de energia Industrial\n')

    if energia_consumida < 5000:
        preco = 0.55
    else:
        preco = 0.60

    valor_a_pagar= energia_consumida * preco
    print('Houve um consumo de', energia_consumida,'kWh de energia')
    print('A industria vai ter que pagar R$', '%.2f' % valor_a_pagar,'de energia consumida')