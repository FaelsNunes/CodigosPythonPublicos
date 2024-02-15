from time import sleep

nome = str(input('Qual seu nome? ')).strip().capitalize()
print('Olá {}, vamos calcular o seu IMC'.format(nome))
print('Preciso que você forneça as informações abaixo')
peso = int(input('\nQual seu peso? '))
#Recebe um float digitado com virgula e converte para número do sistema
altura = (input('Qual sua altura? (Ex. 1,70) '))
altura = float(altura.replace(',','.'))
imc = (peso/(altura*altura))
pimin = 18.5*(altura*altura)
pimax = 24.9*(altura*altura)
pimed = ((pimax-pimin)/2)+pimin
print('\nMuito obrigado pelas informações')
print('PROCESSANDO...')
sleep(3)
print('\nSeu IMC é {}'.format(str(round(imc,2)).replace('.',','))) #Maneira formatada
#print('Seu IMC é {:.2f}'.format(imc)) #Maneira do sistema

if imc < 18.5:
    print('CLASSIFICAÇÃO OFICIAL: ABAIXO DO PESO')
elif imc <= 24.9:
    print('CLASSIFICAÇÃO OFICIAL: PESO IDEAL')
elif imc <= 29.9:
    print('CLASSIFICAÇÃO OFICIAL: SOBREPESO')
elif imc <= 34.9:
    print('CLASSIFICAÇÃO OFICIAL: OBESIDADE I')
elif imc <= 39.9:
    print('CLASSIFICAÇÃO OFICIAL: OBESIDADE II (SEVERA)')
else:
    print('CLASSIFICAÇÃO OFICIAL: OBESIDADE III (MORBIDA)')

print('\n')
if peso >= pimin and peso <= pimax:
    print('Você está dentro do seu limite de peso ideal!'.upper())
else:
    print('Você precisa adequar o seu peso para se encaxar na faixa ideal'.upper())
sleep(4)
print('De acordo com sua altura você deve pesar no mínimo {:.0f}Kg e no máximo {:.0f}Kg'.format(pimin,pimax))
#print('De acordo com sua altura você deve pesar no mínimo {}Kg e no máximo {}Kg'.format(int(pimin),int(pimax)))
sleep(2)
print('Um excelente peso que seria ideal para sua saúde é {:.0f}Kg'.format(pimed))
print('\n----FIM----')
#print('Um excelente peso que seria ideal para sua saúde é {}Kg'.format(int(pimed)))