####################-SINTAXE PYTHON-####################

# Abaixo segue a lista de Operadores
# -> (+) --> Adição
# -> (-) --> Subtração
# -> (*) --> Multiplicação
# -> (/) --> Divisão
# -> (**) --> Potência -> Função interna pow(4,3) -- mas perde a precedência
# -> (//) --> Divisão Inteira
# -> (%) --> Resto da divisão (Valor que sobra da divisão)

# 81**(1/2) #Raiz quadrada de 81
# 81**(1/3) #Raiz cúbica de 81



# Ordem de precedência
# 1 - ()
# 2 - **
# 3 - *,/,//,% #Quem aparecer primeiro entre eles
# 4 - +,- #Quem aparecer primeiro entre eles



#####-FORMATAÇÕES DENTRO DO PRINT-#####
# print('='*20) #Repete o caractere igual por 20 vezes
print('='*50)
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome)) #Faz o nome aparecer em 20 caracteres, se for menor do que 20
print('Prazer em te conhecer {:>20}!'.format(nome)) #Faz o nome aparecer em 20 caracteres, alinhando a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) #Faz o nome aparecer em 20 caracteres, alinhando a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) #Faz o nome aparecer em 20 caracteres, alinhando ao centro
print('Prazer em te conhecer {:=^20}!'.format(nome)) #Faz o nome aparecer em 20 caracteres, alinhando ao centro preenchendo com o caractere que coloquei

######-INÍCIO DO PROGRMA-######
print('-=-' * 15)
titulo = 'A VISTA X PARCELADO'
print('{:^45}'.format(titulo))
print('-=-' * 15)

#{:.3f} -->> Formata um número dentro do print como 3 casas decimais flutuantes



# Abaixo escreve um em cada linha
print('Olá tudo bem com você? ')
print('Como você está? ')

# Abaixo coloca um comando no final do print para na tela juntar as duas linhas (, end=' ') ou (, end='>>>')
print('Olá tudo bem com você? ', end=' ')
print('Como você está? ')

# Abaixo insere um comando que quebra a linha digitada no print (\n)
print('Olá \ntudo bem com você? ')
print('Como \nvocê \nestá? ')



#############INPUTS#############

#Variável recebe valor em branco (vazio)
variavel = ''
variavel = None

#Recebendo um texto e tratando ele
nome = str(input('Digite seu nome: ')).strip().lower()

#Setando um input como float
valordig1 = float(input('Digite um valor: '))

#Recebe um float digitado com virgula e converte para número do sistema
altura = str((input('Qual sua altura? '))).strip()
altura = float(altura.replace(',','.'))

#Recebe valores percentuais com virgula e converte para float
taxa = str(input('Digite a taxa: ')).strip()
taxa = str(taxa.replace(',','.').replace('%',''))


#Divisão na tela
print('===================')
print('='*50)
print('-=-' * 30)
print('\n----FIM----')


#Informações sobre a variável
valordigitado = input('Digite qualquer coisa: ')
print('O que você digitou foi {}'.format(valordigitado))
print('O tipo do objeto é: {}'.format(type(obj))) # Retorna o tipo de objeto
print('Abaixo será retornado algumas informações sobre o que você digitou')
print('É um texto? {}'.format(valordigitado.isalpha()))
print('É alfanumérico? {}'.format(valordigitado.isalnum()))
print('É um número? {}'.format(valordigitado.isnumeric()))
print('Tem codificação ASCII? {}'.format(valordigitado.isascii()))
print('Não sei {}'.format(valordigitado.isdigit()))
print('Está no formato decimal? {}'.format(valordigitado.isdecimal()))
print('É identificável? {}'.format(valordigitado.isidentifier()))
print('Está escrito em minúsculo? {}'.format(valordigitado.islower()))
print('Dá para mostrar em tela? {}'.format(valordigitado.isprintable()))
print('É um espaço? {}'.format(valordigitado.isspace()))
print('É pequeno? {}'.format(valordigitado.istitle()))
print('Foi escrito em letras maiúsculas? {}'.format(valordigitado.isupper()))
#.isdigit() ##Verifica se uma string só possui números

#########################################
#COMO IMPORTAR BIBLIOTECAS
#Importando a biblioteca completa
import math
#Ex. de função: math.trunc()

#Importando só as funções que eu quero
from math import sqrt,pi,ceil,trunc
#Ex. de função: trunc()
#########################################

#BIBLIOTECAS
import emoji #inserir emojis # https://carpedm20.github.io/emoji/all.html?enableList=enable_list_pt
import math #funções matemáticas
import random #números aleatórios e sorteios
import time
import datetime #Dedidado a tempo e datas
from tkinter import * #biblioteca gráfica, cria páginas
from operator import itemgetter #Pega o valor de uma lista/dicionário pelo item Ex-091
import urllib #Biblioteca para trabalhar com internet
import urllib.request #Usado para abrir um site
datetime.date #submódulo dedicado para datas
datetime.time #submódulo dedicado para tempo
datetime.datetime #submódulo dedicado para quando temos tanto tempo como data juntos
datetime.timedelta #usado quando o objetivo é saber a diferença entre períodos de tempos distintos

import pygame #Dedicado a criação de jogos, bom para trabalhos com áudios e imagens


#FÓRMULAS
round(valor,2) #Arredondar por formula, deixar tipo float
int() #Mostra a parte inteira de um número
math.ceil() #Arredordar para cima
math.floor() #Arredondar para baixo
math.sqrt() #Raiz quadrada
math.trunc() #Trunca um número mostrando sua parte inteira
random.random() #Essa função retorna números aleatórios float entre 0 e 1
random.randint(1,10) #Números aleatórios inteiros dentro do intervado
sin(radians(angulo)) #Seno de um angulo após importar a biblioteca math
cos(radians(angulo)) #Cosseno de um angulo após importar a biblioteca math
tan(radians(angulo)) #Tangente de um angulo após importar a biblioteca math
random.choice(lista) #Sortear um valor dentro de uma lista
random.randint(0,5) #Sortear um número entre um intervalo pré definido
random.shuffle(lista) #Embaralha uma lista, depois posso chamar essa lista no print -> print(lista)
time.sleep(3) #Faz o computador esperar 3 segundos para processar o comando abaixo
bin(num)[2:] #Converte um número em binário e exclui os 2 primeiros caracateres (0,1) da visualização pois se tratam do código de identificação
oct(num)[2:] #Converte um número em octal e exclui os 2 primeiros caracateres (0,1) da visualização pois se tratam do código de identificação
hex(num)[2:] #Converte um número em hexadecimal e exclui os 2 primeiros caracateres (0,1) da visualização pois se tratam do código de identificação


'''
Para comentar bloco você utiliza as aspas triplas
'''


#############TRABALHANDO COM DATAS#############

import datetime
data = datetime.date(2023,6,9) #Escreve uma data
print(data) #mostra a data escrita na tela
print(type(data)) #Mostra o tipo da variável data
print(data.ctime()) #Retorna uma outra formatação para a data
dia = data.day #Extrai o dia de uma data
mes = data.month #Extrai o mês de uma data
ano = data.year #Extrai o ano de uma data
ano = date.today().year #Ano atual
#Em dia mês e ano acima, estou pegando uma característica da data, portanto não precisa de parenteses
nova_data = data.replace(month=10) #alterando uma informação de uma data
hoje = datetime.date.today() #Retorna o dia de hoje
ontem = hoje.replace(day=hoje.day - 1) #Retorna o dia de ontem
data_em_texto = '{}/{}/{}'.format(hoje.day, hoje.month, hoje.year) #Uma forma simples de mostrar uma data
delta = hoje - data #subtraindo uma data de outra
datafuturo = hoje+delta #Pegou a diferença de dias calculada acima e somou em outro data
datacompleta.time() #Extrai o horário de uma data completa
hora = datetime.time(12,45,23) #definindo a hora como 12:45:23
h = hora.hour #extrai o número do horário
m = hora.minute #extrai o mínuto do horário
s = hora.second #extrai o segundo ho horário
datatempo = datetime.datetime(2023,6,9,22,20,30) #mistura data e hora, aqui o resultado é: 2023-06-09 22:20:30
agora = datetime.datetime.now() #pega a data e hora atual
anoatual = datetime.date.today().year #Retorna o ano atual
agora_string = agora.strftime("%d/%m/%Y %H:%M:%S") #Formata dia e hora em string. É possível consultar os formatos da função strftime
agora_padrao = datetime.datetime.strptime(agora_string,"%d/%m/%Y %H:%M:%S") #Pega uma data em string e transforma para classe de datetime, necessário colocar o formato exato que está na string
#Para fazer conta com horas, insere as horas no timedelta e utiliza o time delta para o cálculo exemplo abaixo
'''
tt = dt.timedelta(hours=hpadraostr)
t1 = dt.timedelta(hours=h1, minutes=m1)
t2 = dt.timedelta(hours=h2, minutes=m2)
t3 = dt.timedelta(hours=h3, minutes=m3)
hs = tt-(t2-t1)+t3
'''



#####FATIAMENTO DE TEXTO#####
frase = 'Curso em Vídeo Python'
#O python pega cada caractere de texto e define eles em um microespaço
#Toda string a primeira letra é o espaço 0(zero) dentro da cadeira de caracteres
#Obs. O print embaixo é apenas para mostrar na tela, mas o fatiamento não precisa de print
print(frase[9]) #Fatia o texto retornando o caractere cujo ID é 9, ou seja o 10º caractere do texto
print(frase[9:13]) #Retorna os caracteres de ID 9 a 12, pois exclui o 13
print(frase[9:21:2]) #Retorna até o último (pois o último é 20) mas vai pulando duas casas
print(frase[:5]) #Retorna do início(0) até o 4º pois exclui o 5
print(frase[15:]) #Inicia no id 15 e vai até o final
print(frase[9::3]) #Do 9 até o final pulando 3 casas
print(frase[::2]) #Do início até o final, pulando de 2 em 2
f'R${num:.2f}'.replace('.',',') #Pega um número float faz uma formatação e substitui o ponto por virgula
'R${:.2f}'.format(num).replace('.',',') #Pega um número float faz uma formatação e substitui o ponto por virgula


#####ANALISE DE FRASE#####
len(frase) #Conta a quantidade de caracteres
frase.count('o') #Contar quantas vezes aparece a letra "o" minusculas
frase.count('o',0,13) #Conta dentro de um texto fatiado, no caso será o início até o 12
frase.find('deo') #retorna o id da letra de início da ocorrência dentro do texto
frase.rfind('a') #procura a letra a olhando da direita para a esquerda
frase.find('android') #Não encontrará na frase, portanto retornará (-1)
frase.startswith('oi') #Verifica se a frase começa com oi, resultado True ou False
frase.endswith('oi') #Verifica se a frase termina com oi, resultado True ou False
'Curso' in frase #Vai retornar True pois vai encontrar essa palavra dentro da variável frase, se não, seria False
print(cid[0] == 'santo') #Valida se o primeiro nome da cidade é igual a santo
frase.replace('Python','Android') #Substitui o texto, mas não no seu valor original
frase.upper() #Deixa tudo em maisculo
frase.lower() #Deixa tudo em minusculo
frase.capitalize() #Deixa apenas o primeiro caractere em maiusculo e o restante em minusculo
frase.title() #Deixa a letra inicial de cada palavra em maiusculo
frase2 = '   aprenda python  ' #foi inserido 3 espaços iniciais e 2 finais
frase2.strip() #Remove espaços inúteis no início e final da cadeia de caracteres, o resultado será uma nova cadeia de caracteres
frase2.rstrip() #Remove espaços inúteis apenas da direita
frase2.lstrip() #Remove espaços inúteis apenas da esquerda
frase.split() #divide as palavras gerando novas sublistas, gera um id por palavra
frase = '-'.join(frase) #junta cadeia de caracteres separando com traço
frase = ''.join(frase) #junta cadeia de caracteres sem espaço
print(frase.upper().count('O')) #Contar quantas vezes aparece O maiusculo, mudando todas as letras para maiusculo
print(len(frase.strip())) #Conta os caracteres exluindo espaços inúteis
print(frase.replace('Python','Android')) #só altera na tela
frase = frase.replace('Python','Android') #altera a cadeia de texto
print('Curso' in frase) #Analisa se existe a palavra Curso na cadeia de caractere
print(frase.split()) #Quebra a string
dividido = frase.split() #cria-se uma nova variável com a frase dividida por palavras
print(dividido[0]) #Retorna a primeira palavra
print(dividido[2][3]) #mostra a 3º letra da segunda palavra
cpf.zfill(11) #Preenche com zeros a esquerda a variável CPF até que ela fique com 11 caracteres

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ','')
#palavras = frase.split() #separa as palavras
#junto = ''.join(palavras) #junta as palafras sem espaço no meio
fraseinvertida = frase[::-1] #Inverte o texto
# 1º : iNÍNIO / 2º : FIM

print('''
mostra o texto
conforme
eu escrever
ok?
''')



############CONDIÇÃO MANEIRA COMPLETA############
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo')
elif tempo <= 5:
    print('Seu carro ainda dá para o gasto')
else:
    print('Seu carro é velho')
print('--FIM--')

############CONDIÇÃO MANEIRA SIMPLES############
tp = int(input('Quantos anos tem seu carro? '))
print('Carro Novo' if tp <=3 else 'Carro Velho')
print('--FIM--')

############VALIDAR CONDIÇÃO VAZIA############
if not nome: #Valida se existe valor ou se o valor é True, a variável precisa ter sido declarada para funcionar


##########COLOCANDO COR NO TEXTO COM CÓDIGO ANSI##########
'''
Segue abaixo o código quebrado em linha para facilitar o entendimento
print('
       \033[0;30;44m
                    TextoEscrito
                                \033[m')

O código e início e fechamento é o \033[m - para usar dentro do format '\033[m'
entre o colchete e o m, vai os códigos de estilo e cores, separados por ;
'''

'''
´CÓDIGOS DE ESTILO
0 - Sem estilo (Pega o estilo do terminal)
1 - Negrito
4 - Sublinhado
7 - Negativo (inverte as cores de linha e fundo)

CÓDIGOS DE COR DO TEXTO (LETRA)
30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Roxo
36 - Azul claro
37 - Cinza

CÓDIGOS DE COR DO FUNDO
40 - Branco
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul
45 - Roxo
46 - Azul claro
47 - Cinza
'''
print('\033[7;40m Olá, Mundo! \033[m')
a = 3
b = 5
print('Os valores são \033[1;32m{}\033[m e \033[1;31m{}\033[m !!!'.format(a,b))
#Dá para colocar a cor dentro do format também
print('Os valores são {}{}{} e {}{}{}!!!'.format('\033[1;32m',a,'\033[m','\033[1;31m',b,'\033[m'))

#Dá para colocar a cor em variáveis e utilizar as variáveis no format
negritoverde = '\033[1;32m'
negritoamarelo = '\033[1;33m'
negritovermelho = '\033[1;31m'
negritoazulc = '\033[1;36m'
sublinhadoverde = '\033[4;32m'
sublinhadoamarelo = '\033[4;33m'
sublinhadovermelho = '\033[4;31m'
sublinhadoazulc = '\033[4;36m'
corpadrao = '\033[m'
print('Os valores são {}{}{} e {}{}{}!!!'.format(negritoverde,a,corpadrao,negritovermelho,b,corpadrao))

##########################################################

#############ESTRUTURA DE REPETIÇÃO FOR#############

for c in range(0, 6): #Faz a contagem de 0 a 5 - exclui o 6
    print(c) #imprime a contagem
print('Fim') #imprime a mensagem final que está fora do comando de laço

print('\n')

for c in range(6, 0, -1): #Faz a contagem de de 6 a 1 - exclui o 0
    print(c) #imprime a contagem
print('Fim') #imprime a mensagem final que está fora do comando de laço

print('\n')

for c in range(0, 7, 2): #Faz a contagem de 0 a 6 - exclui o 7 - conta de 2 em 2
    print(c) #imprime a contagem
print('Fim') #imprime a mensagem final que está fora do comando de laço

#Faz a contagem usando como limite o número informado pelo usuário
n = int(input('\nDigite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')

print('\n')

#faz a contagem usando todos os elementos informados pelo usuário
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('Fim')

print('\n')

#Recebe diversos valores e vai somando eles
s = 0
for c in range(1, 6):
    n = int(input('Digite o {}º valor: '.format(c)))
    s = s + n #outra maneira de escrever seria -> s += n
print('A soma dos valores digitados é {}'.format(s))

##############################################################
n = c = s = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999: #Quando o valor digitado for o valor de parar
        break #Este comando será executado, saindo do laço e não realizando a soma do 999
    c += 1
    s += n
print(f'A soma dos {c} valores foi {s}!')
print('A soma dos {} valores foi {}!'.format(c,s))

##############################################################

while True: #Vai executar o programa eternamente pois sempre reconhece como verdadeiro
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('_' * 30)
    if n < 0:
        break #este comando faz sair da repetição
    for c in range(1,11): #De 1 a 10
        print(f'{n} X {c} = {n*c}')
    print('_' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

##############################################################
# WHILE INFINITO

print('-' * 40)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)
print('\n')
menorpreco = 10000000.00
prodbarato = ' '
qtde = 0
prodcaro = 0
total = 0
while True:
    nomeprod = str(input('Nome do Produto: ')).strip().capitalize()
    preco = str(input('Preço: R$')).strip()
    preco = float(preco.replace(',','.'))
    qtde += 1
    total += preco
    if preco > 1000:
        prodcaro += 1
    if preco < menorpreco:
        menorpreco = preco
        prodbarato = nomeprod

    continuar = ' ' #Sempre zere a resposta da pergunta antes de perguntar novamente
    #A validação da resposta é incluída antes da pergunta
    while continuar not in 'SN': #Valida se o que foi digitado corresponde ao esperado
        continuar = str(input('Quer Continaur? [S/N] ')).strip().upper()[0] #Se for respondido 'sim' o comando vai pegar só a primeira letra e transformar em maiúscula 'S'

    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA ')) #Funciona para titulos, colocando o texto dentro do tamanho programado
print('O total da compra foi R$ {}'.format(str(total).replace('.',',')))
print('Temos {} produtos custando mais de R$1000,00'.format(prodcaro))
print('O produto mais barato foi {} que custa R${}'.format(prodbarato,str(menorpreco).replace('.',',')))



#################TUPLAS E LISTAS#################

tupla = (1,2) #Não é mutável e não permite adição de valores
lista = [1,2] #É mutável e permite adição de valores

dir(tuple) #Exibe os métodos disponíveis para fazer em tuplas
dir(list) #Exibe os métodos disponíveis para fazer em listas


######################TUPLAS######################

#Tuplas são imutáveis
#Tuplas são variáveis compostas

lanche = ('Hambúrguer','Suco','Pizza','Pudim','Sorvete','Batata Frita','Açaí') #Cria uma tupla
print(lanche) #Exibe a conteúdo completo da tupla
print(lanche[0]) #Exibe o primeiro registro da tupla
print('A tupla tem {} Registros'.format(len(lanche)))
print('\n')

#For usando diretamente a variável composta
for comida in lanche:
    print('Eu vou comer {}'.format(comida))
print('Comi pra caramba!')
print('\n')

#For usando range e variável composta
for cont in range(0, len(lanche)):
    print('Eu vou comer {} na posição {}'.format(lanche[cont], cont))
print('\n')

#Maneira igual a de cima, usando a função enumerate
for pos, comida in enumerate(lanche):
    print('Eu vou comer {} na posição {}'.format(comida, pos))
print('\n')

print(sorted(lanche)) #Imprime os dados da tupla em ordem

a = (2,5,4)
b = (5,8,1,2)
c = a + b #Une as duas tuplas numéricas
d = b + a #Une as duas tuplas numéricas em outra ordem
print(c)
print(d)
print(c.count(5)) #Mostra quantas vezes tem o número 5 dentro da tupla
print(c.index(2)) #Mostra em qual posição está o número 2 dentro da tupla

#tuplas aceitam dados de diferentes tipos
pessoa = ('Rafael',1990,'M', 73.5)
print(pessoa)
del(pessoa) #Tuplas podem ser deletadas

######################LISTAS######################

lista = ['a','b','d'] #Cria uma lista
lista[2] = 'c' #Altera um valor da lista
lista.append('e') #Adiciona um valor no final da lista
lista.insert(3,'d') #Adicionou o valor 'd' na posição 3 da lista
del lista[3] #Apaga um valor da lista pelo índice
lista.pop(3) #Apaga um valor da lista pelo índice
lista.pop() #Por padrão o pop apaga o último item da lista
lista.remove('e') #Apaga um valor da lista pelo próprio valor, se tiver mais de um valor igual, ele remove só o primeiro valor encontrado
teste2 = list(set(teste1)) #Remove dados duplicados de uma lista
if 'f' in lista:
    lista.remove('f') #Avalia se existe o valor antes de removê-lo

lista = list(range(4,11)) #Cria uma lista com base em um range
lista.sort() #Ordena a lista
lista.sort(reverse=True) #Ordena a lista em ordem reversa
len(lista) #Conta quantos elementos existem dentro da lista

from random import shuffle
shuffle(lista) #Embaralha a lista

max(num) #Maior valor em uma lista
min(num) #Menor valor em uma lista

for v in lista:
    print('{}...'.format(v), end='') #Mostra os valores da lista de uma maneira mais bonita

lista1 = lista2 #Iguala uma lista a outra, se alterar uma, também altera a outra, pois é criado vínculo
lista1 = lista2[:] #Lista1 está recebendo todos os valores da lista2, não está criando vínculo

pessoas=[['Pedro',25],['Maria',19],['João',32]] #Uma lista que engloba outras listas
print(pessoas[0][0]) #Imprime "Pedro" na tela, pois é o item 0 da lista 0 que está em pessoas

galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #Adiciona os dados de dado na galera criando uma cópia de dados, sem vínculo
    dado.clear() #Limpa a lista dados para o próximo input
print(galera)

#outra maneira de fazer, já grava os dados como lista de uma única vez
ficha = list()
ficha.append([nome,[nota1,nota2],media]) #Ficha já é uma lista, como configurado aqui, os daos são adicionados com uma lista dentro da lista ficha, e essa lista contém outra lista dentro que são as notas

######################DICIONÁRIOS######################

dados = dict() #declara dicionário
dados = {'nome':'Pedro','idade':25} #declara dicionário
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M' #cria um novo elemento e coloca valor nele
del dados['idade'] #elimina o elemento idade

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
         }

print(filme.values()) #retorna todos os valores de filme
print(filme.keys()) #retorna todas as chaves de filme
print(filme.items()) #retorna todos os valores e chaves de filme

for k, v in filme.items():
    print(f'O {k} é {v}')

#dicionário é mutável
#para dicionar uma cópia do dicionário a uma lista, tem de usar o comando .copy

#exemplo prático

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #copia os valores de um dicionário para uma lista
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

#Lista ranking está recebendo os dados do dicionário jogo, classificando do maior para o menor, olhando pelo valor da chave 1 (valor)
#Para isso antes tem de importar a biblioteca
#Ex-091
from operator import itemgetter #Importação
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True) #Comando

######################FUNÇÕES######################

def lin(): #Define uma função sem parâmetro
    print('-=' * 30)

def mensagem(msg): #define uma função com parâmetro
    print('-=' * 30)
    print(msg)
    print('-=' * 30)

def soma(a, b):
    s = a + b
    print(s)

#Da forma com a função foi feita abaixo, se um valor não for informado, ele recebe zero e não da erro na função
def soma(a=0, b=0, c=0):
    s = a + b
    print(s)

def contador(* núm): #Desempacotamento
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


def soma2(* valores): #Desempacotamento
    s = 0
    for num in valores:
        s += num
    print('Somando os valores {} temos {}'.format(valores,s))

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2 #Está alterando a lista, multiplicando cada número por 2
        pos += 1

#---------------------------------------------------------------------------------
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somapar(lista):
    global a #faz com que o progra utilize uma variável global na função
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista {lista}, temos {soma}')

números = list()

sorteia(números)
somapar(números)
#---------------------------------------------------------------------------------

def voto(ano): #Se não for passado ano, vai ser considerado zero
    """
    Função que analisa se uma pessoa pode votar, analisando a idade dela
    :param ano: Recebe o ano de nascimento da pessoa
    :return: Retorna o status dela em relação ao voto
    """
    from datetime import date #fazer a importação dentro da função economiza memória, fazer caso ela for utilizada somente nessa funç~çao
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NEGADO'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: OPCIONAL'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO'

AnoNascimento = int(input('Que ano você nasceu? '))
print(voto(AnoNascimento))
help(voto) #olha a descrição da formula voto
#---------------------------------------------------------------------------------

######################MINHAS FUNÇÕES######################

def tpf(valor): #Texto para Float
    """
    Essa função pega um número digitado como texto, trata ele e converte para float.
    :param valor: Um número digitado com virgula e ou %/R$
    :return: Valor convertido em float
    """
    #acima eu fiz o arquivo que descreve o que a função faz
    return float(str(valor.strip()).replace(',','.').replace('%','').replace('R$','').replace('$','').replace(' ',''))

numero = str(input('Digite um número com vírgula '))
numero = tpf(numero)
print(numero)
help(tpf) #A função help retorna a descrição de uma função do sistema
#-----------------------------------------------------------------------------------------#

##############################################################

######################TRATAMENTO DE ERROS######################
try: #Comando essencial
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b


##Comando essencial, pode ter vários, forma simples do comando##
#except:
#    print('Erro')


except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: #Comando opicional, executa se deu sucesso, se insucesso não mostra a mensagem de erro do sistema
    print(f'O resultado é {r:.1f}')
finally:#Comando opicional, executa sempre, independente do sucesso
    print('Volte sempre! Muito obrigado!')

######################CRIAR E MODIFICAR ARQUIVOS TXT######################

valoresCelulares = [850,2230,1500,3500,5000,7000]

'''

'r'     -> Usado somente para ler algo
'w'     -> Usado somente para escrever algo substituindo tudo
'a'     -> Usado para acrescentar algo
'r+'    -> Usado para ler e escrever algo 

'''


#Escreve substituindo
with open('valores_celulares.txt','w') as arquivo: #Abre ou cria o arquivo se não existe
    for valor in valoresCelulares: #Para cada item da lista
        arquivo.write(f'{valor}\n') #Escreve no arquivo dando enter

#Escreve adicionando
with open('valores_celulares.txt','a') as arquivo: #Abre ou cria o arquivo se não existe
    for valor in valoresCelulares: #Para cada item da lista
        arquivo.write(f'{valor}\n') #Escreve no arquivo dando enter

#Lê o arquivo
with open('valores_celulares.txt','r') as arquivo: #Abre ou cria o arquivo se não existe
    for valor in arquivo:
        print(valor, end='')

#Lê e escreve no final, mas não adiciona enter
with open('valores_celulares.txt','r+') as arquivo: #Abre ou cria o arquivo se não existe
    for valor in arquivo: #Para cada item da lista
        print(valor)
    arquivo.write('2000') #Escreve no arquivo dando enter
    arquivo.write('\n') #Escreve no arquivo dando enter

######################MANEIRA DO CURSO EM VÍDEO######################

from time import sleep

###########################################

def leiaInt(msg):
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
def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc

###########################################

def arquivoExiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'w+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        #print(a.read()) #Mostra todos os dados como estão
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def escreverArquivo(nome_arquivo,nome,idade):
    try:
        a = open(nome_arquivo, 'a')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
    finally:
        a.close()

def importarArquivo(variavel,nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in a:
            dado = str(linha).replace('\n','')
            variavel.append(dado)
    finally:
        a.close()


def limparArquivo(nome):
    try:
        a = open(nome, 'w') #zera o arquivo
        a.close()
    except:
        print('Houve um erro na abertura do arquivo!')


###########################################

#Programa principal

arq = 'cadastro_pessoas.txt'

#Se o arquivo não existe, cria-se o arquivo
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    #A resposta recebe o valor de "opc" que está na função menu
    resposta = menu(['Ver pessoas cadastradas', 'Cadasatrar nova pessoa', 'Sair do Sistema'])
    #Cada texto acima dentro da lista é uma opção do menu, o título do menu está dentro do função

    #Executa-se a opção selecionada abaixo
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nomePessoa = str(input('Nome: ')).strip().capitalize()
        idadePessoa = leiaInt('Idade: ')
        escreverArquivo(arq,nomePessoa,idadePessoa)
    elif resposta == 3:
        cabecalho('Sainda do sistema... Até logo!')
        break
    else:
        cabecalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

##############################################################
##############################################################

