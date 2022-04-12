#Cauã Hiroshi Dias Tamari T1

nome_de_usuario= input('Digite o nome de usuario: ')
senha= input('Digite sua senha: ')

while(senha == nome_de_usuario):
    print('ERRO! Voce digitou seu nome de usuario')
    senha= input('Digite sua senha: ')

print('Bem vindo,', nome_de_usuario)