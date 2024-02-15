print('**Custo de combustível para viagem**\n')
kmrota = int(input('Quantos Km terá a viagem? (Ida e Volta) '))
#kmlt = float(input('Quantos Km seu veículo faz por litro? '))
kmlt = str(input('Quantos Km seu veículo faz por litro? ')).strip()
kmlt = float(kmlt.replace(',','.'))
#prc = float(input('Qual o preço do combustível? '))
prc = str(input('Qual o preço do combustível? ')).strip()
prc = float(prc.replace(',','.'))
ltn = kmrota/kmlt
custo = ltn*prc
#print('Para fazer essa viagem você gastará R${:.2f} em combustível'.format(custo))
print('Para fazer essa viagem você gastará R${} em combustível'.format(str(round(custo,2)).replace('.',',')))
vt = int(input('\nQuantas vezes este trajeto será feito? '))
ct = vt*custo
print('O custo total será de R${}'.format(str(round(ct,2)).replace('.',',')))