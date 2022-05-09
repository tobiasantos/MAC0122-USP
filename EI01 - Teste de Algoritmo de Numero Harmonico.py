# ===============================================================
"""

Nome: Tobias dos Santos Neto
NUSP: 11848688

Ao incluir esse cabeçalho declaro que todas as partes originais
desse exercício individual foram desenvolvidas e implementadas por
mim e que portanto não constituem desonestidade acadêmica ou plágio.
Declaro também que sou responsável por todas as cópias desse
programa e que não distribui ou facilitei a sua distribuição.
Estou ciente que os casos de plágio e desonestidade acadêmica
serão tratados segundo os critérios divulgados na página da 
disciplina.

Entendo que exercícios sem esse cabeçalho devem receber nota zero
e, ainda assim, poderão ser punidos por desonestidade acadêmica.    
"""
# ===============================================================

def main():
    ''' 
    para testar e descobrir se é possível o valor ser diferente
    de acordo com a forma que o calculamos, basta inserir
    um numero inteiro positivo 'n' que o próprio programa informará se o valor
    calculado sera diferente ou igual ào calculo feito pela outra formula
    '''
    print("testes das funções")
    n = int(input("Digite um numero inteiro positivo: "))
    if Hmenor(n) != Hmaior(n):
        print("Os valores de Hn de ordem %d foram diferentes" %(n))
    else:
        print("Os valores de Hn de ordem %d foram iguais" %(n))
    


def Hmaior(n):
    ''' a função Hmaior() recebe um número inteiro positivo n
    e devolve o valor do número harmônico de ordem 'n'
    calculado do maior termo até o menor termo
    '''
    Hmaior = 0
    cont = 1
    while cont <= n:
        Hmaior += 1/cont
        cont += 1
    return Hmaior


def Hmenor(n):
    ''' a função Hmenor() recebe um número inteiro positivo n
    e devolve o valor do número harmônico de ordem 'n'
    calculado do menor termo até o maior termo
    '''
    Hmenor = 0
    cont = n
    while cont > 0:
        Hmenor += 1/cont
        cont -= 1
    return Hmenor

if __name__ == '__main__':
    main()    
