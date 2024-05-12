'''
Backup de todas as funções que eu criei
'''
def formatar_como_moeda(num):
    """
    -> Pega um número em float, e formata ele como moeda
    Ex. 2.50 -> R$2,50
    :param num: Número em float
    :return: Número formatado como moeda em string
    """
    #n = f'R${num:.2f}'.replace('.',',')
    n = 'R${:.2f}'.format(num).replace('.',',')
    return n

########################################################################################################

def textoparafloat(texto): #Texto para Float
    """
    Essa função pega um número digitado como texto, trata ele e converte para float.
    :param texto: Um número digitado com virgula e ou %/R$
    :return: Valor convertido em float
    """
    return float(str(texto.strip()).replace(',','.').replace('%','').replace('R$','').replace('$','').replace(' ',''))

########################################################################################################

def substituir_em_massa(palavra,lista_de,lista_para):
    """
    Função onde você define o que vai ser substituído e pelo que,
    colocando cada item na mesma ordem, um ao lado do outro, a função substituirá tudo de uma vez

    :param palavra: Palavra ou texto original que se quer tratar
    :param lista_de: colocar entre aspas simples o que se quer substituir, separando por espaço
    Ex: '/ - _'
    :param lista_para: colocar entre aspas simples o que será o novo valor, separado por espaço
    se quiser que o novo valor seja um espaço, escreva esp
    Ex: 'esp . &'
    :return: Retornará a palavra ou frase com os caracteres substituídos

    ATENÇÃO! A mesma quantidade de caracteres passados na "lista_d" deve haver na "lista_para"

    -------------------------------------------------------------------------------------------
    Exemplo prático:

    substituir_em_massa('Bem-Te-Vi, é um pássaro','- é á','esp e a')
    No preenchimento acima, substitui-se '-' por ' ', 'é' por 'e', 'á' por 'a'

    O resultado será: Bem Te Vi, e um passaro

    -------------------------------------------------------------------------------------------
    """
    lista_words = palavra
    lista_d = lista_de.split()
    lista_p = lista_para.split()

    word = lista_words
    if len(lista_d) == len(lista_p):
        for c in range(0,len(lista_d)):
            for d in range(0,len(lista_p)):
                #lista_pp = lista_p[d].replace('esp',' ')
                if c == d:
                    word = word.replace(lista_d[c],(lista_p[d].replace('esp',' ')))
        return word
    else:
        return 'Erro! A quantidade de caracteres informados na lista_d não é a mesma da lista_p'

########################################################################################################

def decimalParaPercentual(num):
    """
    -> Pega um número e divide ele por 100
    :param num: Número fornecido
    :return: Número divido por 100
    """
    return num/100

########################################################################################################

def taxadeequivalencia(taxa,periodoQueTenho='ano',periodoQueQuero='mes'):
    """
    -> Faz a equivalência da taxa do período atual dela para o período desejado
    Caso não for informado os períodos, a equivalência será de anual para mensal

    :param taxa: Digitar a taxa em decimal ex. 12 / 12.5
    :param periodoQueTenho: 'ano'/'mes'/'dia'
    :param periodoQueQuero: 'ano'/'mes'/'dia'
    :return: Taxa equivalente ao período desejado. Escrita em decimal (0.94 = 0,94% / 1 = 1%)
    """
    tx = decimalParaPercentual(taxa)

    if periodoQueTenho == 'ano':
        ntc = 360
    elif periodoQueTenho == 'mes':
        ntc = 30
    elif periodoQueTenho == 'dia':
        ntc = 1

    if periodoQueQuero == 'ano':
        nqc = 360
    elif periodoQueQuero == 'mes':
        nqc = 30
    elif periodoQueQuero == 'dia':
        nqc = 1

    return (((1+(tx))**(nqc/ntc)-1)*100)

########################################################################################################
def data_hora_atual():
    import datetime
    agora = datetime.datetime.now() #pega a data e hora atual
    agora = datetime.datetime(agora.year,agora.month,agora.day,agora.hour,agora.minute,agora.second)
    return agora

########################################################################################################

def titulo(msg):
    print('-=' * ((len(msg) // 2) + 2))
    print('  {:^}'.format(msg))
    print('-=' * ((len(msg) // 2) + 2))

########################################################################################################

def leiaInt(msg):
    """
    Faz a leitura de um número inteiro, função do Gustavo Guanabara
    :param msg:
    :return:
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

########################################################################################################

def linha(tam = 42):
    """
    Printa uma linha, se não for definido o tamanho, ele será 42, função do Gustavo Guanabara
    :param tam:
    :return:
    """
    return '-' * tam

########################################################################################################

def menu(lista):
    """
    Cria um menu automático e já armazena a opção escolhida, para utilizar essa função, utilize no programa principal o seguinte comando

    ex. resposta = menu(['Opção 1, 'Opção 2'])

    :param lista:
    :return:
    """
    titulo('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc

########################################################################################################
def posicaoTela():
    import pyautogui
    import time

    time.sleep(5)
    print(pyautogui.position())