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

ABRE = '([{'
FECHA = ')]}'
def main():
    ''' função para teste da função bem_formada
    '''
    # testes
    print("(a+{b})-{2*[3+4]} é bem formada? Resposta esperada: True")
    print(bem_formada( "(a+ {b })-{2*[3+4]}" ))
    print('\n')
    print("((() é bem formada? Resposta esperada: False")
    print(bem_formada("( ( (  ) "))
    print('\n')
    print("{({x})}[y] é bem formada? Resposta esperada: True")
    print(bem_formada(" { ( { x } )  } [ y ]"))
    print('\n')
    print("{({x}}[y]) é bem formada? Resposta esperada: False")
    print(bem_formada(" { ( { x }  } [ y ] )"))
    print('\n')
    print("{[a+(b+(c+b)+d)]} é bem formada? Resposta esperada: True")
    print(bem_formada("{[a+(b+(c+b)+d)]}"))
    print('\n')
    lista_testes = ['( [ ] ) [ ] { }', '( [ ] [ ] { }', '( [ { ( [ ] ) } ] )', '( ( [ ) { } ] )', '[ { } { } ( [ ] { { } } ]', '( ( ( [ [ { } ] ] ) { } ) ) [ ( { } ) ] { }', '[ } [] { { }', '( [ { [ ] [ ] } ] ) ( { } { } ) ( [ ] )', '( ( ) [ ( ) ] )', '( [ ) ]']
    for item in lista_testes:
        print(f"{item} : {bem_formada(item)}")
# ---------------------------------------------------------

def bem_formada( seq ):
    ''' (str) -> bool
    Recebe uma string seq contendo uma sequência formada pelos
    caracteres '()[]{}'. 
    Retorna True caso a sequência esteja bem formada e False em
    caso contrário.
    A função deve ignorar caracteres diferentes de '()[]{}' 
    sem resultar em erro.
    Exemplos:
    >>> bem_formada( "(a+ {b })-{2*[3+4]}" )
    True
    >>> bem_formada( "( ( (  ) " )
    False
    >>> bem_formada( " { ( { x } )  } [ y ]" )
    True
    >>> bem_formada( " { ( { x }  } [ y ] )" )
    False
    '''
    s = []
    bemformada = True
    indice = 0
    identificador = ''
    while indice < len(seq) and bemformada:
        simbolo = seq[indice]
        if simbolo in ABRE:
            s.append(simbolo)
        if simbolo in FECHA:
            if len(s) == 0:
                bemformada = False
            else:
                for i in range(len(FECHA)):
                    if FECHA[i] == simbolo:
                        identificador = i
                if s[len(s) - 1] == ABRE[identificador]:
                    s.pop()
                else:
                    s.append(simbolo)
        elif simbolo == '$':
            if s == [] or s[-1] != '$':
                s.append(simbolo)
            elif s[-1] == '$':
                s.pop()
        indice += 1
    if len(s) == 0 and bemformada:
        return True
    else:
        return False
# ---------------------------------------------------------

if __name__ == '__main__':
    main()