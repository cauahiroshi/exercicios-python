#Cauã Hiroshi Dias Tamari T1

distancia = float(input('Qual distancia voce deseja percorrer? '))

if distancia <= 200.0:
    preco_passagem = distancia * 1.0
    print('A viagem vai custar R$', preco_passagem)
else:
    preco_passagem = distancia * 0.5
    print('A viagem vai custar R$', preco_passagem)