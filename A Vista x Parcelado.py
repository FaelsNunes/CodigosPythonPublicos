print('-=-' * 15)
titulo = 'A VISTA X PARCELADO'
print('{:^45}'.format(titulo))
print('-=-' * 15)
print('''
Se você quer comprar um bem e tem o dinheiro para pagá-lo a vista
este programa faz uma análise para lher dizer se é melhor pagar o bem a vista
ou comprar ele parcelado, investir o dinheiro do valor a vista,
e sacar do investimento mensalmente o valor das parcelas
''')

#Entrada dos dados
precoavista = str(input('Qual o preço a vista do bem a ser comprado? R$ ')).strip()
precoavista = float(precoavista.replace(',','.'))
qtdeparcela = int(input('Qual a quantidade de parcelas para pagamento? '))
precoparcela = str(input('Qual o valor da parcela? R$ ')).strip()
precoparcela = float(precoparcela.replace(',','.'))
print('\nA taxa do CDI (Taxa DI) pode ser encontrata no site: b3.com.br')
cdiano = str(input('Qual a taxa do CDI ANUAL que está vigente neste momento? ')).strip()
cdiano = float(cdiano.replace(',','.').replace('%',''))
opcaoinv = int(input('\nO investimento que você pretende fazer do valor a vista paga: 1 - % do CDI / 2 - % Fixo? '))
if opcaoinv < 1 or opcaoinv > 2:
 print('OPÇÃO INVÁLIDA! REINICIE O PROGRAMA!')
elif opcaoinv == 1:
 taxainv = str(input('Qual o % do CDI que o investimento paga? ')).strip()
 taxainv = float(taxainv.replace(',','.').replace('%',''))
 taxainv = ((cdiano/100) * (taxainv/100))*100 #Pega o CDI e aplica a taxa de % do CDI, obendo a taxa de investimento anual
else:
 opcaotxinv = int(input('A taxa do seu investimento é: 1 - Anual / 2 - Mensal? '))
 if opcaotxinv < 1 or opcaoinv > 2:
  print('OPÇÃO INVÁLIDA! REINICIE O PROGRAMA!')
 elif opcaotxinv == 1:
  taxainv = str(input('Qual o % que o seu investimento paga? ')).strip()
  taxainv = float(taxainv.replace(',','.').replace('%',''))
 else:
  taxainv = str(input('Qual o % que o seu investimento paga? ')).strip()
  taxainv = float(taxainv.replace(',','.').replace('%',''))
  taxainv = (((1 + (taxainv/100)) ** (360/30)) -1)*100 #Transforma a taxa do investimento de mensal para anual

taxainvmensal = (((1 + (taxainv/100)) ** (30/360)) -1) * 100 #Pega a taxa do investimento anual e a transforma em mensal
precoparcelado = qtdeparcela * precoparcela
capitalinicial = precoavista
capitalfinal = 0
pmt = 0
juros = 0
somajuros = 0
difpgparcelado = round(precoparcelado - precoavista,2)
dados = []

print('\n')
for c in range(0, qtdeparcela + 1):
 if c == 0:
  print('{:^3} | {:^15} | {:^10} | {:^10} | {:^15}'.format('PMT','CAPITAL INICIAL','PARCELA','JUROS','CAPITAL FINAL'))
  somajuros = round(juros + capitalinicial * (taxainvmensal/100),2)
  juros = round(capitalinicial * (taxainvmensal/100),2)
  capitalfinal = round(capitalinicial + juros,2)
  dados.append((pmt,capitalinicial,0,juros,capitalfinal))
  print('{:^3} | {:^15} | {:^10} | {:^10} | {:^15}'.format(str(pmt).replace('.',','),'R$ '+str(capitalinicial).replace('.',','),'R$ 0','R$ '+str(juros).replace('.',','),'R$ '+str(capitalfinal).replace('.',',')))
 else:
  pmt = pmt + 1
  capitalinicial = capitalfinal
  juros = round((capitalinicial - precoparcela) * (taxainvmensal/100),2)
  juros = juros if juros >= 0 else 0
  somajuros = round(somajuros + juros,2)
  capitalfinal = round(capitalinicial + juros - precoparcela,2)
  dados.append((pmt,capitalinicial,precoparcela,juros,capitalfinal))
  print('{:^3} | {:^15} | {:^10} | {:^10} | {:^15}'.format(str(pmt).replace('.',','),'R$ '+str(capitalinicial).replace('.',','),'R$ '+str(precoparcela).replace('.',','),'R$ '+str(juros).replace('.',','),'R$ '+str(capitalfinal).replace('.',',')))

#Resultado final
resultado = somajuros - difpgparcelado
print('\n')
print('Preço a Vista R${}'.format(str(precoavista).replace('.',',')))
print('Preço Parcelado R${}'.format(str(precoparcelado).replace('.',',')))
print('Diferença entre os preços R${}'.format(str(abs(difpgparcelado)).replace('.',',')))
print('Receita de Juros R${}'.format(str(somajuros).replace('.',',')))
print('\n')
if resultado < 0:
 print('Compensa PAGAR A VISTA, pois a diferença entre o preço parcelado e o preço a vista é maior do que a receita com os juros do investimento.')
else:
 print('Compensa INVESTIR o dinheiro do pagamento a vista, e sacar o valor das parcelas para paga-las mensalmente, dessa maneira você pagará o bem e ainda lhe sobrará R${} no final.'.format(str(round(somajuros-difpgparcelado,2)).replace('.',',')))

print('\nOBS. NÃO ESTÁ SENDO DESCONTADO OS IMPOSTOS INCORRENTES NOS INVESTIMENTOS')
print('\n')
print('-----FIM-----')
