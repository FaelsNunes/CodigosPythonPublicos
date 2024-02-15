from math import log

#Apresentação inicial
print('\033[1;30;46m CALCULADORA DE JUROS COMPOSTOS \033[m')
print('\033[1mA informação abaixo que você não informar (0), será calculada\033[m')
print('\033[1mDas 4 opções, você deve digitar 3, deixando apenas uma com 0\033[m')

#Entrada de valores
valorpresente = str(input('\nDigite o valor presente (Quer descobrir? -> digite 0): '))
valorpresente = float(valorpresente.replace(',','.'))

valorfuturo = str(input('Digite o valor futuro (Quer descobrir? -> digite 0): '))
valorfuturo = float(valorfuturo.replace(',','.'))

taxa = str(input('Digite a taxa (Quer descobrir? -> digite 0): '))
taxa = float(taxa.replace(',','.').replace('%',''))/100

periodo = str(input('Digite o periodo (Quer descobrir? -> digite 0): '))
periodo = float(periodo.replace(',','.'))

#Valida informações digitadas
validapresente = 1 if valorpresente > 0 else 0
validafuturo = 1 if valorfuturo > 0 else 0
validataxa = 1 if taxa > 0 else 0
validaperiodo = 1 if periodo > 0 else 0
somavalidacao = validapresente + validafuturo + validataxa + validaperiodo

#Se houver erro de preenchimento retorna o tipo do erro
if somavalidacao == 4:
    print('\nVocê preencheu todos os valores, não tem o que analisar!'.upper())
if somavalidacao < 3:
    print('\nVocê não digitou a quantidade de critérios necessários!'.upper())
else:
    print('\n')
    if valorpresente == 0:
        vp = valorfuturo / (1+taxa) ** periodo
        print('O valor presente é R${:.2f}'.format(vp))
    if valorfuturo == 0:
        vf = valorpresente * (1+taxa) ** periodo
        print('O valor futuro é R${:.2f}'.format(vf))
    if taxa == 0:
        tx = ((valorfuturo/valorpresente) ** (1/periodo) -1)*100
        print('A taxa é {:.4f}%'.format(tx))
    if periodo == 0:
        n = ((log(valorfuturo/valorpresente))/log(1+taxa))
        print('O período é {:.2f}'.format(n))
print('\n')
print('\033[1;30;46m-----FIM-----\033[m')