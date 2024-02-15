from FuncoesRnb import numbers

print('-=-' * 30)
print('{:^90}'.format('TAXA DE EQUIVALÊNCIA'))
print('-=-' * 30)

#Levanta o valor da taxa que eu tenho
txtenho = str(input('\nQual o valor da taxa que você tem? ')).strip()
#txtenho = float(txtenho.replace(',','.').replace('%',''))
txtenho = numbers.textoparafloat(txtenho)

#Transforma a taxa em decimal
#txtenhodec = txtenho/100
txtenhodec = numbers.decimalParaPercentual(txtenho)

#Levanta o período da taxa que eu tenho
nt = 0
while nt < 1 or nt > 3:
    nt = int(input('Qual o período que está a taxa que você tem? [1-Ano / 2-Mês / 3-Dia] '))

#Levanta o período que eu quero
nq = 0
while nq < 1 or nq > 3:
    nq = int(input('Para qual período você quer converter a taxa? [1-Ano / 2-Mês / 3-Dia] '))

#Gera o valor de cálculo correspondente ao período escolhido, e o texto do nome do período
if nt == 1:
    ntc = 360
    ntt = 'Ano'
elif nt == 2:
    ntc = 30
    ntt = 'Mês'
else:
    ntc = 1
    ntt = 'Dia'

#Gera o valor de cálculo correspondente ao período escolhido, e o texto do nome do período
if nq == 1:
    nqc = 360
    nqt = 'Ano'
elif nq == 2:
    nqc = 30
    nqt = 'Mês'
else:
    nqc = 1
    nqt = 'Dia'

#Realiza o cálculo da taxa de equivalência
taxaequivalente = (((1+(txtenhodec))**(nqc/ntc)-1)*100)
taxaequivalente = round(taxaequivalente,4)
taxaequivalente = str(taxaequivalente).replace('.',',')

print('\nVocê informou a taxa de {}% ao {}, ela equivale a taxa de {}% ao {}.\n'.format(str(txtenho).replace('.',','),ntt,taxaequivalente,nqt))
print('-=-' * 30)