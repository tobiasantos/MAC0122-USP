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
    '''
    print("Testes da classe Array2d\n")

    # beginfora
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    print('teste 1: Criação do Array2d a:')
    print(a)
    print()

    b = a.reshape( (2,3) )   
    print('teste 2: reshape cria uma vista')
    print(b)
    print()
    
    print('teste 3: mudanças em b devem resultar em mudanças em a:')
    b[1, 2] = 100
    print(a)
    print(b)
    print()

    print('teste 4: e vice-versa - mudanças em a devem resultar em mudanças em b:')
    a[0, 2] = -1 
    print(a)
    print(b)
    print()

    print('teste 5: copy cria um clone')
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    c = a.copy()
    print(f'a: {a}')
    print(f'c: {c}')
    print()

    print('teste 6: mudanças em objeto um não devem refletir no outro')
    a[0,1] = 99
    c[0,5] = -1
    print(f'a: {a}')
    print(f'c: {c}')
    print()

    print('teste 7: carregue')
    lista = [1,2,3,4,5,6]
    a = Array2d( (2,3), 0)
    print(f'a:\n{a}\n')

    a.carregue( lista )
    print(f'a:\n{a}\n')

    a[1,1] = -1
    print(f'a:\n{a}\n')
    print(f'lista: {lista}')
    print()

    print('teste 8: carregue2')
    lista = [1,2,3,4,5,6]
    a = Array2d( (2,3), 0)
    print(f'a:\n{a}\n')

    a.carregue2( lista )
    print(f'a:\n{a}\n')

    a[1,1] = -1
    print(f'a:\n{a}\n')
    print(f'lista: {lista}')
    print()

    print('teste 9: flipV')
    lista = [1,2,3,4,5,6,7,8,9,0]
    a = Array2d( (5,2), 0)
    a.carregue( lista )
    print(f'a:\n{a}\n')

    flip = a.flipV()
    print(f'flip:\n{flip}\n')

    print(f'a:\n{a}\n')
    print()

    print('teste 10: flipH')
    lista = [1,2,3,4,5,6,7,8,9,0]
    a = Array2d( (2,5), 0)
    a.carregue( lista )
    print(f'a:\n{a}\n')

    flipH(a)
    print(f'a:\n{a}\n')
    
    '''
    print("Testes da classe Array2d e comparação com Numpy\n")

    lista_a = [1, 2, 3, 4, 5, 6]
    lista_b = [0, 1, 1, 0, 0, 1]
    tam_a = len(lista_a)
    tam_b = len(lista_b)

    a = Array2d( (1, tam_a), 0) # cria Array2d com valor inicial 0
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print()
    a.data = lista_a   ## ou a.carregue(lista_a) como no EG10
    a.resize( (2,3) )
    print(f'a:\n{a}\n')

    b = Array2d( (1, tam_b), 0)
    b.data = lista_b   # ou b.carregue(lista_b)
    b.resize( (3,2) )
    print(f'b:\n{b}\n')

    linha = a.getlin(0)
    print(f'linha a.getlin(0)\n{linha}\n')

    coluna = b.getcol(1)
    print(f'coluna b.getcol(1)\n{coluna}\n')

    print(f'linha.dot(coluna)\n{linha.dot(coluna)}\n')

    print(f'matmul(a,b)\n{matmul(a,b)}\n')

    ### agora com Numpy
    import numpy as np
    npa = np.array( lista_a ).reshape((2,3))
    print(f'npa:\n{npa}\n')

    npb = np.array( lista_b ).reshape((3,2))
    print(f'npb:\n{npb}\n')

    print(f'np.matmul(npa, npb):\n{np.matmul(npa, npb)}\n')
    print('ao invés de np.matmul podemos usar @:')
    print(f'npa @ npb:\n{npa @ npb}\n')

## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.

class Array2d:

    # ---------------------------------------------------------------
    def __init__(self, shape, val):
        ''' (Array2d, tuple, obj) -> None
        Constrói um objeto do tipo Array2d com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da matriz
        size : número total de elementos da matriz
        '''
        self.shape = shape
        self.size = shape[0]*shape[1]
        self.data = []
        if type(val) == int or type(val) == float:
            for i in range(self.size):
                self.data.append(val)
        if type(val) == list:
            for elemento in val:
                self.data.append(elemento)

    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (Array2d, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do Array2d self.

        Esse método é usado quando o objeto é chamado com 
        uma tupla entre colchetes, como self[0,0]. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> a[1,1] + 100
        99
        >>> print( a[1,1] )
        -1
        '''
        return self.data[self.shape[1]*key[0] + key[1]]

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (Array2d, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do Array2d self.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`, como self[0,0] = 0. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> print( a[1,1] )
        -1
        >>> a[1,1] = 100
        >>> print( a[1,1] )
        100
        '''
        self.data[self.shape[1]*key[0] + key[1]] = valor

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2d) -> None
        ao ser usada pela função print, deve exibir cada linha
        do Array2d em uma linha separada, separando seus elementos por um espaço.

        Exemplo: para self.data = [1, 2, 3, 4, 5, 6] e self.shape = (2,3)
        o método deve retornar a string 
        "1 2 3\n4 5 6" 
        e, caso self.shape = (3,2) o método deve retornar a string
        "1 2\n3 4\n5 6" 
        '''
        string = ''
        i = 0
        for a in range(self.shape[0]):
            for b in range(self.shape[1]):
                string += f"{self.data[i]} "
                i += 1
            string += '\n'
        return string
    # ---------------------------------------------------------------
    # Escreva outros métodos e funções caso desejar
    
    def copy(self):
        ''' (Array2d) -> Array2d
        recebe um objeto da classe Array2d e devolve uma cópia do mesmo
        objeto
        '''
        return Array2d(self.shape, self.data)
    # ---------------------------------------------------------------
    def reshape(self, key):
        '''(tupla) -> Array2d
        recebe uma tupla e reorganiza um Array2d seguindo a nova tupla
        informada para definir o numero de linhas e colunas
        '''
        a = Array2d(key, self.data)
        a.data = self.data
        return a
  # ---------------------------------------------------------------
    def carregue(self, nova_lista):
        ''' (Array2d, lst) -> None
        recebe uma Array2d e uma lista. Atualiza a data da array para
        uma vista da nova_lista
        '''
        self.data = nova_lista
    # ---------------------------------------------------------------
    def carregue2(self, nova_lista):
        ''' (Array2d, lst) -> None
        recebe uma Array2d e uma lista. Atualiza a data da array para
        um clone da nova_lista
        '''
        self.data = nova_lista[:]
     # ---------------------------------------------------------------
    def flipV(self):
        '''
        '''
        a = self.copy()
        nlins, ncols = self.shape
        for i in range(nlins // 2):
            for j in range(ncols):
                x = a.data[i * ncols + j]
                y = a.data[(nlins - 1 - i) * ncols + j]
                a.data[(nlins - 1 - i) * ncols + j] = x
                a.data[i * ncols + j] = y
        return a
    # ---------------------------------------------------------------
    def getlin(self, lin):
        '''(Array2d, int) -> Array2d
        '''
        a  = []
        nlin, ncol = self.shape
        for i in range(ncol*lin,ncol*(lin+1)):
            a.append(self.data[i])
        x = Array2d((1,ncol), a)
        return x
    # ---------------------------------------------------------------
    def getcol(self, col):
        '''(Array2d, int) -> Array2d
        '''
        a = []
        nlin, ncol = self.shape
        for i in range(col, self.size, ncol):
            a.append(self.data[i])
        x = Array2d((nlin,1),a)
        return x
    # ---------------------------------------------------------------
    def dot(self,other):
        '''(Array2d, Array2d) -> int/float
        '''
        soma = 0
        for i in range(self.size):
            soma += self.data[i]*other.data[i]
        return soma
    # ---------------------------------------------------------------
    def resize(self, key):
        '''(Array2d, tupla) -> None
        recebe uma tupla e reorganiza um Array2d seguindo a nova tupla
        informada para definir o numero de linhas e colunas
        '''
        self.shape = key
# ---------------------------------------------------------------
def flipH(array):
    '''
    '''
    nlins, ncols = array.shape
    for j in range(ncols // 2):
        for i in range(nlins):
            x = array.data[i * ncols + j]
            y = array.data[i * ncols + ncols - 1 - j]
            array.data[i * ncols + ncols - 1 - j] = x
            array.data[i * ncols + j] = y
# ---------------------------------------------------------------
def matmul(esq,direita):
    '''(Array2d, Array2d) -> Array2d
    '''
    a = []
    m1 = 0
    m2 = 0
    elemento = 0
    for i in range(esq.shape[0]):
        for j in range(direita.shape[1]):
            m1 = esq.getlin(i)
            m2 = direita.getcol(j)
            elemento = m1.dot(m2)
            a.append(elemento)
    x = Array2d((esq.shape[0],direita.shape[1]), a)
    return x
# ---------------------------------------------------------------
def marque_regiao(ar, esq, sup, direita, inf, valor=0):
    '''(Array2d, int, int, int, int, num) -> None
    Recebe um objeto Array2d e par de inteiros (esq,sup) 
     que indica o canto esquerdo-superior e o par de 
     inteiros (dir,inf) que indica o canto direito-inferior 
     de uma região do Array2d e preenche os elementos dessa 
     região com "valor"
     '''
    for i in range(sup,inf):
        for j in range(esq,direita):
            ar[i,j] = valor
# ---------------------------------------------------------------
def marque_regiao_np(ar, esq, sup, direita, inf, valor=0):
     '''(np.ndarray, int, int, int, int, num) -> None
     Recebe um ndarray do Numpy, um par de inteiros (esq,sup) 
     que indica o canto esquerdo-superior e o par de inteiros 
     (dir, inf) que indica o canto direito-inferior de uma 
     região do Array e preenche os elementos dessa região com "valor". 
     '''
     ar[sup:inf,esq:direita] = valor
# ---------------------------------------------------------------
def rotacione( ar ):
    ''' (Array2d) -> None
    Recebe um Array2d ar de dimensão quadrada e retorna None.
    Antes de retornar, gira ar de 90 graus no sentido anti-horário.
    '''
    lst = []
    for i in range(ar.shape[1]-1,-1,-1):
        a = ar.getcol(i)
        lst += a.data
    ar.data = lst
# ---------------------------------------------------------------
def rotacione_np( ar ):
    ''' (np.ndarray) -> None
    Recebe um np.ndarray ar de dimensão quadrada e retorna None.
    Antes de retornar, gira ar de 90 graus no sentido anti-horário.
    '''
    nlin, ncol = ar.shape
    lst= []
    for i in range(ncol -1, -1, -1):
        lista = []
        for j in ar[:,i:i+1]:
            lista.append(int(j))
        lst.append(lista)
    ar[:,:] = lst
    #ar[:,:] = lst
            
    #    lst.append(ar[:,i:i+1])
    #ar[:,:] = lst
    
    
        
## ==================================================================

if __name__ == '__main__':
    main()