tpoper = int(input('Qual o tipo da operação? (1-NOVO / 2-PORT / 3-REFIN) '))
qtdeparc = int(input('Qual a quantidade de parcelas? '))
principaloper = str(input('Digite o valor principal da operação: R$ ')).strip()
principaloper = float(principaloper.replace(',','.'))

#Se a operação for Novo/Port o liberado é igual ao principal, se não, pergunta-se o liberado
if tpoper == 1 or tpoper == 2:
	liberadooper = principaloper
else:
	liberadooper = str(input('Qual o valor atual da operação que será refinanciada? R$ ')).strip()
	liberadooper = float(liberadooper.replace(',','.'))
	liberadooper = principaloper - liberadooper

taxaoper = str(input('Qual a taxa da operação? ')).strip()
taxaoper = float(taxaoper.replace(',','.').replace('%',''))
taxaoperok = taxaoper / 100

#Calcula o valor da parcela
prestacao = (principaloper*taxaoperok*(1+taxaoperok)**qtdeparc)/((1+taxaoperok)**qtdeparc-1)

################################################################################################

capitalinicial = capitalfinal = periodo = vlrjuros = somavlrjuros = amortizacao = somaamortizacao = 0

for c in range(0, qtdeparc + 1):
	if c == 0:
		print('\n')
		capitalinicial = principaloper
		capitalfinal = principaloper
		print('{:^10} | {:^20} | {:^10} | {:^10} | {:^10} | {:^10} | {:^20}'.format('PERÍODO','CAPITAL INICIAL','TAXA','PARCELA','JUROS','AMORTIZAÇÃO','CAPITAL FINAL'))
		print('{:^10} | {:^20} | {:^10} | {:^10} | {:^10} | {:^10} | {:^20}'.format(periodo,round(capitalinicial,2),round(taxaoper,2),0,0,0,round(capitalfinal,2)))
	else:
		capitalinicial = capitalfinal
		periodo	= periodo + 1
		vlrjuros = capitalinicial * taxaoperok
		amortizacao = prestacao	- vlrjuros
		capitalfinal = capitalinicial - amortizacao
		somavlrjuros = somavlrjuros + vlrjuros
		somaamortizacao += amortizacao
		print('{:^10} | {:^20} | {:^10} | {:^10} | {:^10} | {:^10} | {:^20}'.format(periodo,round(capitalinicial,2),round(taxaoper,2),round(prestacao,2),round(vlrjuros,2),round(amortizacao,2),round(capitalfinal,2)))

################################################################################################

print('\nO valor da parcela será R${}'.format(round(prestacao,2)))
print('O total de juros a ser pago é R${}'.format(round(somavlrjuros,2)))
print('O total amortizado é R${}'.format(round(somaamortizacao,2)))
print('O total da operação é R${}'.format(round(somaamortizacao	+ somavlrjuros,2)))
print('O valor disponibilizado para você será R${}'.format(round(liberadooper,2)))
