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

## ==================================================================

def main():

    print("Testes das suas funções recursivas \n")
    print("Testes da maxR: \n")
    print(f"maxR([12,17,15]): {maxR([12,17,15])} -> Deve ser 17")
    print(f"maxR([-4,-7,-19]): {maxR([-4,-7,-19])} -> Deve ser -4")
    print(f"maxR([14,32]): {maxR([14,32])} -> Deve ser 32 \n")
    print("Testes da somaR: \n")
    print(f"somaR([12,-15,7]): {somaR([12,-15,7])} -> Deve ser 4")
    print(f"somaR([1,3,5,7]): {somaR([1,3,5,7])} -> Deve ser 16")
    print(f"somaR([-2,-4,-6]): {somaR([-2,-4,-6])} -> Deve ser -12")
    print(f"somaR([0,12,1]): {somaR([0,12,1])} -> Deve ser 13")
    

## ------------------------------------------------------------------

def maxR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna o valor do maior elemento.
        Exemplos: 
        - para a entrada [12, 15, 7], a funcao deve retornar 15.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar None.

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa max() do Python para resolver esse exercício.
    '''
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        return lista[0]
    maximo = lista[-1]
    if maximo > maxR(lista[:-1]):
        return maximo
    if maximo < maxR(lista[:-1]):
        return maxR(lista[:-1])
## ------------------------------------------------------------------

def somaR( lista ):
    ''' (list) -> int
        recebe uma lista de numeros inteiros e retorna a soma de todos os elementos da lista.
        Exemplo: 
        - para a entrada [12, -15, 7], a funcao deve retornar 4.
        - para a entrada [51], a funcao deve retornar 51.
        - para a entrada [], a funcao deve retornar 0 (zero).

        OBS: Esse é um exercício para treinar a aplicação de recursão. Por isso,
        não use a função nativa sum() do Python para resolver esse exercício.
    '''
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return lista[0]
    soma = lista[0]
    return soma + somaR(lista[1:])

## ------------------------------------------------------------------
def somaR2(lista,n):
    if n == 0:
        return 0
    ultimo = lista[n-1]
    soma_do_resto = somaR2(lista, n-1)
    return ultimo + soma_do_resto

if __name__ == '__main__':
    main()