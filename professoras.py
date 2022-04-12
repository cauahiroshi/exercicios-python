#Cauã Hiroshi Dias Tamari T1

# A estrutura de repetição for permite que voce consiga percorrer elementos em um array. 
# a estrutura dele é o for, a variavel que vai indicar determinado elemento na lista (representada pelo n)
# e por fim o nome da lista que voce carrega os elementos 

#No código a baixo eu declaro a lista com o nome das minha professoras, exibo o nome das professoras 
# e por fim eu uso uma função para indicar qual aula determinada professora da 

import modulo_materias

professoras = ['Juliana', 'Thais', 'Jadi', 'Paola', 'Tais', 'Natalia']

for n in professoras:
    print(n)
    modulo_materias.materias_das_professoras(n)
    
    