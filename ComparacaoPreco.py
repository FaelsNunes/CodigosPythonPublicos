print('\033[1;32mCOMPARADOR DE PREÇOS PELO CUSTO DA UNIDADE\033[m')
print('\n')

minprec = 100000000.00
nomprecmin = prod = ' '
idt = qtdeprecmin = vlmprecmin = idv = precoprodwin = 0
listacomparacao = []

while prod != 'Fim':
    idt = idt + 1
    prod = str(input('\033[1;32mNOME\033[m do produto {}: [P/ Terminar dig. \033[1;31m"fim"\033[m] '.format(idt))).strip().capitalize()
    if prod == 'Fim':
        break
    qtde = int(input('\033[1;32mQUANTIDADE\033[m de itens da embalagem: '))
    vlme = str(input('\033[1;32mVOLUME/TAMANHO\033[m da unidade do produto: ')).strip()
    vlme = float(vlme.replace(',','.'))
    prec = str(input('\033[1;32mPREÇO\033[m do produto: R$ ')).strip()
    prec = float(prec.replace(',','.'))
    preu = round((prec/(qtde*vlme)),5)
    listacomparacao.append([preu,prod,qtde,vlme,prec,idt])

    if preu < minprec:
        minprec = preu
        nomprecmin = prod
        qtdeprecmin = qtde
        vlmprecmin = vlme
        precoprodwin = prec
        idv = idt

    print('\n')
print('\n')

listacomparacao.sort()

ind = 0
print('{:^4} | {:^20} | {:^4} | {:^8} | {:^8} | {:^10}'.format('RANK','NOME PRODUTO','QTDE','VOLUME','PREÇO','PREÇO UN'))
for c, i in enumerate(listacomparacao):
    ind += 1
    print('{:^4} | {:^20} | {:^4} | {:^8} | {:^8} | {:^10}'.format(ind,listacomparacao[c][1],listacomparacao[c][2],listacomparacao[c][3],listacomparacao[c][4],round(listacomparacao[c][0],6)))

print('\n')
print('\033[1;32m-=-\033[m' *30)
print('O {}º produto digitado:\n\nNome: {} | Quantidade: {} | Volume: {} | Preço: R${}\n\nÉ o que tem a unidade mais barata, com preço unitário de R${}.'.format(idv,nomprecmin,qtdeprecmin,str(vlmprecmin).replace('.',','),str(precoprodwin).replace('.',','), str(minprec).replace('.',',')))
print('\033[1;32m-=-\033[m' *30)
