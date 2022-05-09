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


import numpy as np

## ------------------------------------------------------------------
def main():
    

    '''print("Testes da classe NPImagem\n")
    
    lista = list(range(20))
    ar = np.array(lista).reshape(4,5)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem( (4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}\n")

    img2[1,2] = -10
    print(f"img2[1,2]={img2[1,2]}")
    print(f"img2:\n{img2}\n")

    img3 = img2.crop() ## cria uma cópia
    print(f"img3:\n{img3}\n")

    img4 = img1.crop(0, 1, 3, 4)  
    print(f"img4:\n{img4}\n")

    img5 = NPImagem( (3,2) )
    print(f"img5:\n{img5}\n")

    img6 = img1.crop(1,2)
    print(f"img6:\n{img6}\n")
    
    lista = list(range(20))
    ar = np.array(lista).reshape(4,5)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}")
    print(f'elemento[0,0] ==> img1[0,0] = {img1[0,0]}')
    print(f'elemento[0,1] ==> img1[0,1] = {img1[0,1]}')
    print()
    
    img2 = NPImagem( (4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}\n")

    img2[1,2] = -10
    print(f"img2[1,2]={img2[1,2]}")
    print(f"img2:\n{img2}\n")

    img3 = img2.crop() ## cria uma cópia
    print('img3 é cópia de img2')
    print(f"img3:\n{img3}\n")
    print()
    print('Se altero img2 NÃO deve alterar img3')
    print()
    print('img2[0,0] = 234')
    img2[0,0] = 234
    print()
    print(f'img2 = \n{img2}')
    print()
    print(f'img3 = \n{img3}')
    
    print()
    img4 = img1.crop(0, 1, 3, 4)  
    print('img4 = img1.crop(0, 1, 3, 4)')
    print(f"img4:\n{img4}\n")
    print()
    print('img5 = NPImagem( (3,2) ) por padrão, val = 0')
    img5 = NPImagem( (3,2) )
    print(f"img5:\n{img5}\n")
    print()
    img6 = img1.crop(1,2)
    print('img6 = img1.crop(1,2)')
    print(f"img6:\n{img6}\n")
    '''
    lista = list(range(30))
    ar = np.array(lista).reshape(5,6)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")
    
    img2 = NPImagem( (3, 2), 100)
    img3 = img2.crop() ## cria uma cópia
    img2[2,1] = -10
    print(f"img2[1,2]={img2[2,1]}")
    print(f"img2:\n{img2}\n")
    print(f"img3:\n{img3}\n")
    
    img1.pinte_retangulo(1,2,3,5,99)
    print(f"img1.pinte_retangulo(1,2,3,5,99):\n{img1}\n")
    
    img2.pinte_retangulo(-1,-2,1,2,88)
    print(f"img2.pinte_retangulo(-1,-2,1,2,88):\n{img2}\n")
    
    img3.pinte_retangulo(1,0,3,4,77)
    print(f"img3.pinte_retangulo(1,0,3,4,77):\n{img3}\n")
    
    img1.paste(img2, 1, 2)
    print(f"img1.paste(img2,1,2):\n{img1}\n")
    
    img1.paste(img3, 3, 5)
    print(f"img1.paste(img3,3,5):\n{img1}\n")
    
    img1.paste(img3, -1, -1)
    print(f"img1.paste(img3,-1,-1):\n{img1}\n")
    


## ------------------------------------------------------------------
class NPImagem():

    # escreva aqui os métodos da classe NPImagem
    def __init__(self, shape, val=0):
        '''(NPImagem, tuple, obj) -> None
        Constrói um objeto do tipo NPImagem com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da imagem
        '''
        if type(val) == int or type(val) == float:
            self.shape = shape
            self.data = np.full(shape,val)
        elif type(val) == np.ndarray:
            self.data = val
            self.shape = val.shape
    # ---------------------------------------------------------------
    def __str__(self):
        '''(NPImagem) -> str
        '''
        return f"{self.data}"
    # ---------------------------------------------------------------
    def __getitem__(self,key):
        '''(NPImagem, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do NPImagem self.
        '''
        return self.data[key[0],key[1]]
    # ---------------------------------------------------------------
    def __setitem__(self,key,valor):
        '''(NPImagem, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do NPImagem self.
        '''
        self.data[key[0],key[1]] = valor
    # ---------------------------------------------------------------
    def crop(self,sup= 0, esq= 0, inf = 'vazio' , direita = 'vazio'):
        '''(NPImagem, int, int, int, int) -> NPImagem
        recebe um objeto da classe NPImagem e 4 inteiros responsáveis pelas
        coordenadas de uma nova região que será determinada dentro de NPImagem
        devolve essa nova região como cópia de NPImagem self.
        '''
        if inf == 'vazio':
            inf = self.shape[0]
        if direita == 'vazio':
            direita = self.shape[1]
        lin, col, nlin, ncol = sup, esq, inf, direita
        a = np.copy(self.data[lin:nlin,col:ncol])
        img = NPImagem((),a)
        return img
    # ---------------------------------------------------------------
    def pinte_retangulo(self, sup, esq, inf, direita, v=0):
        '''(NPImagem, int, int, int, int, int) -> None 
        Recebe 4 inteiros que definem o canto superior-esquerdo (sup, esq) e
        o canto inferior-direito (inf,dir) de uma região retangular com 
        relação a posição (0,0) de self, ou seja, os cantos são "deslocamentos" 
        em pixeis com relação à origem.
        Esse método pinta, com o valor v, os pixeis de self que tenham sobreposição
        com o retângulo (sup,esq)x(inf,dir). 
        '''
        if sup < 0:
            sup = 0
        if esq < 0:
            esq = 0
        self.data[sup:inf,esq:direita] = v
    # ---------------------------------------------------------------  
    def paste(self, other, sup, esq):
         '''(NPImagem, NPImagem, int, int) -> None
         Recebe um objeto NPImagem other e par de inteiros (sup, esq) 
         que indica um deslocamento em relação à origem de self (posição (0,0)) 
         onde a NPImagem other deve ser sobreposta sobre self. Observe que
         esse deslocamento pode ser negativo.
         '''
         for i in range(other.shape[0]):
             for j in range(other.shape[1]):
                 if sup+i<self.shape[0] and esq+j<self.shape[1]:
                    if 0<=sup+i<=self.shape[0] and 0<=esq+j<=self.shape[1]:
                        self[sup+i,esq+j]=other[i,j]
     
        
        
## ------------------------------------------------------------------
## ------------------------------------------------------------------
if __name__ == '__main__':
    main()
