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


class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.
 
       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve se "comportar" ilustrados no enunciado.
    '''
    def __init__(self, hora = 0, minu = 0, seg = 0):
        horario = []
        horario.append(seg)
        horario.append(minu)
        horario.append(hora)
        self.dados = horario
        for i in range(len(self.dados)):
            if self.dados[i] >= 60:
                self.dados[i+1] += self.dados[i]//60
                self.dados[i] %= 60
        if self.dados[2] >= 24:
            self.dados[2] %= 24
        
    def __str__(self):
        relogio = []
        for i in range(len(self.dados)):
            if self.dados[i] < 10:
                relogio.append('0' + str(self.dados[i]))
            else:
                relogio.append(str(self.dados[i]))
        return f"{relogio[2]}:{relogio[1]}:{relogio[0]}"
    
    def __add__(self, other):
        new_hora = self.dados[2] + other.dados[2]
        new_min = self.dados[1] + other.dados[1]
        new_seg = self.dados[0] + other.dados[0]
        return Horario(new_hora, new_min, new_seg)
    
    def __sub__(self, other):
        self_hora = self.dados[2]
        self_min = self.dados[1]
        self_seg = self.dados[0]
        new_seg = self_seg - other.dados[0]
        if new_seg < 0: 
            self_min -= 1 # retira 1 minuto para ganhar 60 segundos
            self_seg += 60 
            if self_min < 0:
                self_min += 1 # devolve o minuto que foi retirado
                self_hora -= 1 # retira 1 hora para ganhar 60 minutos
                self_min += 59 # converte 1h em 59 minutos
                if self_hora < 0:
                    self_hora += 1 # devolve a hora que foi retirada
                    self_min -= 59 # devolve os 59 minutos adicionados
                    self_seg -= 60 # devolve os 60 segundos adicionados
                    return Horario() # valor vazio, pois não há valores negativos
            new_seg = self_seg - other.dados[0]
        new_min = self.dados[1] - other.dados[1]    
        if new_min < 0:
            self_hora -= 1 # retira 1 hora para ganhar 60 minutos
            self_min += 60
            if self_hora < 0:
                    self_hora += 1 # devolve a hora retirada
                    self_min -= 60 # devolve os 60 minutos adicionados
                    return Horario() # valor vazio, pois não há valores negativos
            new_min = self_min - other.dados[1]
        new_hora = self_hora - other.dados[2]
        if new_hora < 0:
            return Horario() # valor vazio, pois não há valores negativos
        return Horario(new_hora, new_min, new_seg)
                   
    def __eq__(self, other):
        igualdade = True
        for i in range(len(self.dados)):
            if self.dados[i] != other.dados[i]:
                igualdade = False
        return igualdade
    
    def __gt__(self, other):
        superioridade = True
        if self.dados[2] < other.dados[2]:
            superioridade = False
        if self.dados[2] == other.dados[2]:
            if self.dados[1] < other.dados[1]:
                superioridade = False
            if self.dados[1] == other.dados[1]:
                if self.dados[0] <= other.dados[0]:
                    superioridade = False
        return superioridade
    
    def __lt__(self, other):
        inferioridade = True
        if self.dados[2] > other.dados[2]:
            inferioridade = False
        if self.dados[2] == other.dados[2]:
            if self.dados[1] > other.dados[1]:
                inferioridade = False
            if self.dados[1] == other.dados[1]:
                if self.dados[0] >= other.dados[0]:
                    inferioridade = False
        return inferioridade
    
    def __ge__(self, other):
        superioridade = True
        if self.dados[2] < other.dados[2]:
            superioridade = False
        if self.dados[2] == other.dados[2]:
            if self.dados[1] < other.dados[1]:
                superioridade = False
            if self.dados[1] == other.dados[1]:
                if self.dados[0] < other.dados[0]:
                    superioridade = False
        return superioridade
    
    def __le__(self,other):
        inferioridade = True
        if self.dados[2] > other.dados[2]:
            inferioridade = False
        if self.dados[2] == other.dados[2]:
            if self.dados[1] > other.dados[1]:
                inferioridade = False
            if self.dados[1] == other.dados[1]:
                if self.dados[0] > other.dados[0]:
                    inferioridade = False
        return inferioridade
    
def main():

    t1 = Horario(8,0,0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1,40)
    print(f't2 = {t2} e deve ser 01:40:00')
    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')
    t4 = t1 + Horario(0,100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00') 
    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 >  t2} e deve ser True')
    print(f't1 >= t2 é {t1 >= t2} e deve ser True')
    print(f't1 <  t2 é {t1 <  t2} e deve ser False')
    print(f't1 <= t2 é {t1 <  t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')
    t5 = Horario(23,59,59)
    t6 = Horario(0,0,1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 00:00:00')
    t8 = t1 - t2  
    print(f't8 = {t8} e deve ser 06:20:00')
    t9 = t2 - t1   ##   nao temos horarios negativos
    print(f't9 = {t9} e deve ser 00:00:00')
    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')

## CASO VOCÊ UTILIZE ESSA FUNÇÃO MAIN 
## NAO SE ESQUEÇA DE TERMINAR O SEU ARQUIVO COM
if __name__ == '__main__':
    main()          

