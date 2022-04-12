#Cauã Hiroshi Dias Tamari T1

# Esse programa imprimir a quantidade de numeros fibonacci que o usuario pedir 
# O while é uma estrutura de repetição que repete o loop enquanto sua condição for verdadeira

quantidade = int(input('Quantos numeros você deseja imprimir? '))

primeiro_numero = 0
segundo_numero = 1

contador = 1

while contador <= quantidade: 
    print(primeiro_numero)

    resultado = primeiro_numero + segundo_numero
    primeiro_numero = segundo_numero
    segundo_numero = resultado

    contador += 1
    