# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Tobias dos Santos Neto
    NUSP: 11848688

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que trabalhos sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    
    Estou ciente que os casos de plágio e desonestidade acadêmica
    estarão sujeitos às penalidades descritas na página da disciplina
    na seção "Sobre colaboração em MAC0122".

    Reconheço que utilizei as seguintes fontes externas ao conteúdo 
    utilizado e recomendado em MAC0122, ou recebi auxílio das pessoas
    listadas abaixo.

    - LISTA de fontes externas utilizadas (links ou referências como livros)
        - 

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''
from timeit import default_timer as timer
## ==================================================================

def fibonacciR(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma recursiva.
    Retorna o valor calculado.

    Exemplos:
    fibonacciR(5) = 5
    fibonacciR(10) = 55
    fibonacciR(20) = 6765
    fibonacciR(30) = 832040
    fibonacciR(40) = 102334155
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    ultimo, penultimo = fibonacciR(n-1), fibonacciR(n-2)
    return ultimo + penultimo

## ==================================================================

def fibonacciI(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma iterativa.
    Retorna o valor calculado.
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    ultimo = 1
    penultimo = 0
    for i in range(n-1):
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual
    return atual

def main():
    for i in range(10,51,10):
        start = timer()
        f = fibonacciR(i)
        end = timer()
        print(f"O tempo para calcular fibonnaciR({i}) foi {end-start} segundos.")
    for i in range(10,51,10):
        start = timer()
        f = fibonacciI(i)
        end = timer()
        print(f"O tempo para calcular fibonnaciI({i}) foi {end-start} segundos.")


main()
    