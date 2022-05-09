# -*- coding: utf-8 -*-
# 
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Tobias dos Santos Neto
    NUSP: 11848688

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
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
        - O texto sugerido para o AP02 o qual falava sobre o Teorema de Euclides.
        

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''

# ===================================================================

def main():
    '''
        Programa main usado para teste da classe Fraction.
    '''

    # Criação de objetos do tipo Fraction 
    f12 = Fraction(1,2)
    f34 = Fraction(3,4)

    # soma 2 fracoes
    soma = f12 + f34
    print(f"{f12} + {f34}      = {soma}")
    print(f"Resultado esperado = 5/4 ")

    # soma fracao com inteiro
    soma = f12 + 2
    print(f"{f12} + 2         = {soma}")
    print(f"Resultado esperado = 5/2 ")

    # soma inteiro com fracao
    soma = 2 + f34
    print(f"  2 + {f34}      = {soma}")
    print(f"Resultado esperado = 11/4 ")
    
    # divisao de duas fracoes
    f1 = Fraction(1,2)
    f2 = Fraction(3,4)
    div = f1/f2
    print(f"{f1} / {f2}      = {div}")
    print(f"Resultado esperado = 2/3")
    
    # divisao de fracao por inteiro
    f1 = Fraction(1,2)
    div = f1/3
    print(f"{f1} / 3      = {div}")
    print(f"Resultado esperado = 1/6")
    
    # divisao de inteiro por fracao
    f1 = Fraction(1,3)
    div = 2/f1
    print(f"2 / {f1}      = {div}")
    print(f"Resultado esperado = 6/1")
    
    # igualdade entre fracoes multiplas
    f1 = Fraction(5,4)
    f2 = Fraction(10,8)
    print(f"5/4 == 10/8      = {f1 == f2}")
    print(f"Resultado esperado = True")
    
    # igualdade entre fracao e inteiro
    f1 = Fraction(6,1)
    print(f"{f1} == 6     = {f1 == 6}")
    print(f"Resultado esperado = True")
    
    # igualdade entre inteiro e fracao
    f1 = Fraction(4,1)
    print(f"4 == {f1}     = {4 == f1}")
    print(f"Resultado esperado = True")
    
    # comparacao entre duas fracoes
    f1 = Fraction(2,5)
    f2 = Fraction(3,6)
    print(f"{f1} > {f2}     = {f1>f2}")
    print(f"Resultado esperado = False")
    
    # comparacao entre fracao e inteiro
    f1 = Fraction(3,1)
    f2 = Fraction(4,1)
    print(f"{f1} > 1     = {f1>1}")
    print(f"Resultado esperado = True")
    print(f"{f2} <= 10     = {f2<=10}")
    print(f"Resultado Esperado = True")
    print(f"3 > {f1}      = {f1.__rgt__(3)}")
    print(f"Resultado Esperado = True")
    print(f"2 <= {f2}     = {f2.__rle__(2)}")
    print(f"Resultado Esperado = True")
    # ===================================================================
    # Escreva outros testes


# ===================================================================
#
#   No futuro substituiremos a definição da classe por um import. 
#
# ===================================================================

class Fraction:
    '''
        Essa classe Fraction foi adaptada da seção 1.13.1 Uma Classe Fraction
        do capítulo 1 do livro Resolução de Problemas com Algoritmos e 
        Estruturas de Dados usando Python disponível no endereço
        https://panda.ime.usp.br/panda/static/pythonds_pt/index.html. 

        A classe Fraction representa uma fração. 
        Uma fração é constituída por um numerador e um denominador, 
        ambos inteiros, como por exemplo 2/5 (dois quintos), 
        onde 2 é o numerador e 5 o denominador.
    '''
           
    def __init__(self, cima = 0, baixo = 1):
        '''(Fraction, int, int) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os inteiros cima e baixo que representam
        a fração.

        Exemplos:

        >>> frac = Fraction(2,5) # construtor chama __init__()
        >>> frac.num
        2
        >>> frac.den
        5
        '''
        self.num = cima//self.meu_mdc(cima, baixo)
        self.den = baixo//self.meu_mdc(cima,baixo)
        
    def meu_mdc( self, a, b ):
        ''' (Fraction, int, int) -> int 
        recebe dois inteiros a e b, e 
        retorna o mdc entre a e b.
        '''
        aa = abs(a)
        ab = abs(b)
        mdc = min(aa, ab)
        if mdc == 0:
            return max(aa, ab)
        while (aa % mdc != 0) or (ab % mdc != 0): 
            mdc -= 1
        return mdc

    def __str__(self):
        '''(Fraction) -> str

        Recebe uma referencia `self` a um objeto da classe Fraction e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplo:

        >>> frac = Fraction(2,5)
        >>> print(frac)
        2/5
        '''
        return f"{self.num}/{self.den}"

    #------------------------------------
    def __add__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a soma da Fraction `self` e da Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction + Fraction ou
                                            Fraction + int
        """
        if type(other) is int:
            novonum = self.den*other + self.num
            novoden = self.den
        else:
            novonum = self.num*other.den + self.den*other.num
            novoden = self.den*other.den
        
        return Fraction(novonum, novoden)

    #------------------------------------
    def __radd__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a soma da Fraction `self` e int `other`.
        Usado pelo Python quando escrevemos int + Fraction
        """
        
        return self + other
        

    #-------------------------------------
    def __truediv__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a divisão da Fraction `self` pela Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction / Fraction ou
                                            Fraction / int
        """
        if type(other) is int:
            novonum = self.num
            novoden = self.den*other
        else:
            novonum = self.num*other.den
            novoden = self.den*other.num
        
        return Fraction(novonum, novoden)

    #-------------------------------------
    def __rtruediv__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a divisão do int `other` pela Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """
        novonum = other*self.den
        novoden = self.num
        
        return Fraction(novonum, novoden)


    #-------------------------------------
    def __eq__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a comparação da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction == Fraction ou
                                            Fraction == int
        """
        if type(other) is int:
            if self.den == 1 and self.num == other:
                return True
            else:
                return False
        else:
            if self.num*other.den == self.den*other.num:
                return True
            else:
                return False

    #-------------------------------------
    def __req__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a comparação do int `other` com a Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """
        return self == other
    #-------------------------------------
    def __gt__(self, other):
        """ (Fraction, Fraction ou int) -> Bool
        
        Retorna uma comparação entre o `self` e o `other`        
        e informa se 'self' é maior que 'other'
        Usado pelo Python quando escrevemos Fraction > Fraction ou int.
        """
        if type(other) is int:
            if self.num/self.den > other:
                return True
            else:
                return False
        else:
            if self.num/self.den > other.num/other.den:
                return True
            else:
                return False
    #-------------------------------------
    def __rgt__(self, other):
        """ (Fraction, int) -> Bool
        
        Retorna uma comparação entre o `other` e o `self`
        e informa se 'other' é maior que 'self'
        Usado pelo Python quando escrevemos int > Fraction.
        """
        if other > self.num/self.den:
            return True
        else:
            return False
    #-------------------------------------
    def __le__(self, other):
        """ (Fraction, Fraction ou int) -> Bool
        
        Retorna uma comparação entre o `self` e o `other`
        e informa se 'self' é menor ou igual ao 'other'
        Usado pelo Python quando escrevemos Fraction <= Fraction ou int.
        """
        if type(other) is int:
            if self.num/self.den <= other:
                return True
            else: 
                return False
        else:
            if self.num/self.den <= other.num/other.den:
                return True
            else:
                return False
    #-------------------------------------
    def __rle__(self, other):
        """ (Fraction, int) -> Bool
        
        Retorna uma comparação entre o `other` e o `self`
        e informa se 'other' é menor ou igual ao 'self'
        Usado pelo Python quando escrevemos int >= Fraction.
        """
        if other <= self.num/self.den:
            return True
        else:
            return False
   
      
        
        

## =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================
if __name__ == "__main__":
    main()