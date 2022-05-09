#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome:Tobias dos Santos Neto
    NUSP: 11848688

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim ou por meu time 
    cujos nomes estão relacionados abaixo e que, portanto, não 
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
    listadas abaixo, e incluo também os nomes de colegas
    do meu time caso essa tenha sido uma atividade em grupo.

    - LISTA de colegas do time 
        - não foi uma atividade em grupo (substitua essa linha caso tenha sido)

    - LISTA de fontes externas utilizadas (links ou referências como livros)
        - 

    - LISTA de outras pessoas que colaboraram na realização do trabalho e
        externas ao grupo.
        - 
'''

# ===================================================================

def main():
    '''
        Programa main usado para teste da classe Fraction 
        e pode ser usada também para testar as suas funções
        HFmaior e HFmenor, que devem usar obrigatoriamente a
        classe Fraction.

        Execute esse programa antes de escrever suas funções e
        estude a saída de cada teste da classe Fraction abaixo, 
        lendo os comentários para entender o comportamento da classe 
        antes de escrever suas funções HFmaior() e HFmenor().  
    '''

    # Criação de objetos do tipo Fraction 
    frac25 = Fraction(2,5)
    print(f"Fraction(2,5) = {frac25}")

    frac12 = Fraction(1,2)
    frac13 = Fraction(1,3)
    frac01 = Fraction(   )  # chamada 'sem' argumentos para testar valores default

    # chamada direta do método __str__() -- não fazemos isso normalmente!!
    print(f"frac01.__str__() = {frac01.__str__()}")
    # mas podemos usar o str() que chama o método __str__
    print(f"str(frac01) = {str(frac01)}")
    # e a função print() também chama o __str__ automaticamente
    # essas chamadas ficam "escondidas" para facilitar a leitura do código.
    print(f"Fraction()    = {frac01}")

    print(f"Fraction(1,2) = {frac12}")
    print(f"Fraction(1,3) = {frac13}")

    # métodos distintos para soma de duas frações
    print(f"frac12 + frac13 = {frac12 + frac13}")
    print(f"frac12.some(frac13) = {frac12.some(frac13)}")

    # hmmm usar o operador + parece mais fácil... 
    # como fica com atribuição?
    soma = frac12 + frac13
    print(f"soma = {soma}")
    soma = soma + frac25
    print(f"soma = {soma}")

    ### coloque aqui os testes para as funções HFmaior e HFmenor
    n = 10
    hma = HFmaior(n)
    print(f"Resultado de HFmaior({n}) = {hma}")
    hme = HFmenor(n)
    print(f"Resultado de HFmenor({n}) = {hme}")

# ===================================================================

def HFmaior( n ):
    ''' 
    (int) -> fraction
    recebe um inteiro positivo e devolve o n�mero harm�nico de ordem 'n'
    escrito em fra��o calculado do maior termo at� o menor
    '''
    Hmaior = Fraction()
    cont = 1
    while cont <= n:
        Hmaior += Fraction(1,cont)
        cont += 1
    
    return Hmaior

# ===================================================================

def HFmenor( n ):
    ''' 
    (int) -> fraction
    recebe um inteiro positivo e devolve o n�mero harm�nico de ordem 'n'
    escrito em fra��o calculado do menor termo at� o maior
    '''
    Hmenor = Fraction()
    cont = n
    while cont > 0:
        Hmenor += Fraction(1,cont)
        cont -= 1
        
    return Hmenor

# ===================================================================


# ===================================================================
#   No futuro substituiremos a definição da classe por um import. 
#   Como primeiro exercício de POO, leia o código da classe Fraction 
#   abaixo e verifique o quanto esse código é semelhante ao do livro. 
#   
#   NÃO ALTERE O CÓDIGO DA CLASSE FRACTION
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

    def __init__(self, cima=0, baixo=1):
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
        >>> f01 = Fraction() # construtor chama __init__()
        >>> f01.num
        0
        >>> f01.den
        1
        '''
        self.num = cima
        self.den = baixo

    def __str__(self):
        '''(Fraction) -> str

        Recebe uma referencia `self` a um objeto da classe Fraction e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplos:

        >>> frac = Fraction(2,5)
        >>> frac.__str__()
        '2/5'
        >>> print(frac)
        2/5
        '''
        return f"{self.num}/{self.den}"

    def some(self,other):
        ''' (Fraction, Fraction) -> Fraction

        Recebe uma referencia `self` a um objeto da classe Fraction e
        outra referência `other` para outro objeto da classe Fraction, e
        cria e retorna um objeto da classe Fraction contendo a soma das
        frações self e other.

        Exemplo:
        >>> f0 = Fraction(1, 2)
        >>> f1 = Fraction(1, 3)
        >>> f3 = f0.some(f1)
        >>> print(f3)
        5/6
        '''
        novonum = self.num*other.den + self.den*other.num
        novoden = self.den * other.den
        return Fraction(novonum,novoden)

    def __add__(self,other):
        ''' (Fraction, Fraction) -> Fraction

        Recebe uma referencia `self` a um objeto da classe Fraction e
        outra referência `other` para outro objeto da classe Fraction, e
        cria e retorna um objeto da classe Fraction contendo a soma das
        frações self e other.

        O __add__ é um método especial, indicados pelo par caracteres
        underscores (`__`) antes e depois da palavra `add`, que substitui
        o operador `+` usado para soma de objetos da classe Fraction.

        Exemplo:
        >>> f0 = Fraction(1, 2)
        >>> f1 = Fraction(1, 3)
        >>> f3 = f0.some(f1)
        >>> print(f3)
        5/6
        '''
        novonum = self.num*other.den + self.den*other.num
        novoden = self.den * other.den
        return Fraction(novonum,novoden)


## =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================
if __name__ == "__main__":
    main()