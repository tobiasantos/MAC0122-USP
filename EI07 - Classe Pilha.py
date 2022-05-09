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
## Escreva a sua função palindromo()

def palindromo( s ):
    ''' (str) -> bool
    Recebe um elemento str e devolve um elemento bool que informa se o str é,
    ou não, um palíndromo.
    '''
    a = str(s)
    a = a.lower()
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for letra in a:
        if letra in ['á', '´à', 'ã']:
            a = a.replace(letra, 'a')
        elif letra in ['é', 'ê']:
            a = a.replace(letra, 'e')
        elif letra in ['í', 'î']:
            a = a.replace(letra, 'i')
        elif letra in ['ó', 'ô', 'õ']:
            a = a.replace(letra, 'o')
        elif letra in ['ú', 'û']:
            a = a.replace(letra, 'u')
        elif letra not in alfabeto:
            a = a.replace(letra, '')
            
    verificador = Pilha()
    for i in range(len(a)):
        verificador.empilhe(a[i])
    check = Pilha()
    n = len(a)-1
    while n >= 0:
        check.empilhe(a[n])
        n -= 1
    if check.dados == verificador.dados:
        return True
    else:
        return False
## ==================================================================
##
class Pilha:

    def __init__(self):
        ''' (Pilha, int/float/str/bool) -> None
        recebe um elemento e o adiciona em uma Pilha.
        '''
        pilha = []
        self.dados = pilha
        
    def __str__(self):
        '''(Pilha) -> str
        Recebe uma referencia `self` a um objeto da classe Pilha e
        cria e retorna a string que representa o objeto.
        '''
        return f"{self.dados}"
    
    def __len__(self):
        ''' (Pilha) -> int
        Recebe um objeto da classe Pilha e retorna um número inteiro referente
        ao comprimento da Pilha.
        '''
        comp = 0
        for i in range(len(self.dados)):
            comp += 1
        return comp
    def vazia(self):
        ''' (Pilha) -> bool
        Recebe um objeto da classe Pilha e retorna uma variável booleana
        informando se o comprimento da pilha é igual ou diferente de 0.
        '''
        if len(self.dados) == 0:
            return True
        else:
            return False
        
    def empilhe(self, elemento):
        ''' (int/float/str/bool/list) -> None
        recebe um elemento int/float/str/bool/list e o insere no topo da Pilha
        em questão
        '''
        self.dados.append(elemento)
        
    def topo(self):
        '''(Pilha) -> int/float/str/bool/list
        recebe um objeto da classe Pilha e devolve o elemento de maior índice
        dessa Pilha
        '''
        return self.dados[len(self.dados)-1]
    
    def desempilhe(self):
        '''(Pilha) -> int/float/str/bool/list
        recebe um objeto da classe Pilha e devolve o elemento de maior índice
        dessa Pilha, além de removê-lo da mesma.
        '''
        return self.dados.pop(len(self.dados)-1)
                       
def testes():

    pil = Pilha()   ## cria uma Pilha vazia
    print(f"pil.dados = {pil.dados}  --> deve ser a lista vazia []")
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser True")
    pil.empilhe('todos')
    pil.empilhe(4)
    pil.empilhe('paz')
    # Pilha.topo() apenas pega o valor no topo mas sem desempilher
    print(f"pil.topo() = {pil.topo()}  --> deve ser 'paz'") 
    pil.empilhe(True)
    print(f"len(pil) = {len(pil)} --> deve ser 4")  ## implemente o método __len__
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser False")
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz', True]")
    pil.empilhe(2.7)
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser 2.7")
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser True")
    print(f"len(pil) = {len(pil)} --> deve ser 3") 
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz']")
    
def bem_formada( s ):
    ''' (str) -> bool
    recebe uma string s contendo uma sequência de abre e fecha parênteses
    e retorna True caso a sequência esteja bem formada e False caso contrário.

    Exemplos:
    >>> bem_formada('(')
    False
    >>> bem_formada(')(')
    False
    >>> bem_formada('(()))(')
    False
    >>> bem_formada('()()')
    True
    >>> bem_formada('(())')
    True
    '''
    l1 = Pilha()
    for i in range(0,len(s),1):
        if s[i] == "(":
            l1.empilhe(s[i])
        
    for i in range(0,len(s),1):
        if s[i] == ")":
            if l1.vazia() == False:
                l1.desempilhe() 
            else:
                l1.empilhe(")")
                
    return l1.vazia()
    
        
        
        
        
    
   
    
## ==================================================================
## Escreva outras funções e classes caso desejar
def main():
    print(f"Olé! Maracujá, caju, caramelo! é palíndromo --> True : {palindromo('Olé! Maracujá, caju, caramelo!')}")
    print(f"Socorram-me, subi no ônibus em Marrocos! é palíndromo --> True : {palindromo('Socorram-me, subi no ônibus em Marrocos!')}")
    print(f"Eva, asse essa ave! é palíndromo --> True : {palindromo('Eva, asse essa ave!')}")
    print(f"MAC0122 não é palíndromo --> False : {palindromo('MAC0122')}")

## ==================================================================
main()
if __name__ == '__main__':
    palindromo( '' )

