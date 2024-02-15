valorinvestido = str(input('Qual o valor que será investido? R$ ')).strip()
valorinvestido = float(valorinvestido.replace(',','.'))

opcao = 0
if opcao not in (1,2):
    opcao = int(input('VOCÊ QUER: 1 - Definir os meses do investimento / 2 - Definir o valor final do investimento? '))

if opcao == 1:
    mesesinvestimento = int(input('Quantos meses o valor ficará investido? '))
else:
    metainvestimento = str(input('Qual o valor que deseja retirar no final do investimento? R$ ')).strip()
    metainvestimento = float(metainvestimento.replace(',','.'))

#Abaixo é definido a taxa do investimento
opcaoinv = int(input('\nO investimento que você pretende fazer do valor a vista paga: 1 - % do CDI / 2 - % Fixo? '))
if opcaoinv < 1 or opcaoinv > 2:
    print('OPÇÃO INVÁLIDA! REINICIE O PROGRAMA!')
elif opcaoinv == 1:
    print('\nA taxa do CDI (Taxa DI) pode ser encontrata no site: b3.com.br')
    cdiano = str(input('Qual a taxa do CDI ANUAL que está vigente neste momento? ')).strip()
    cdiano = float(cdiano.replace(',','.').replace('%',''))
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

juros = capitalfinal = periodo = somajuros = qtdeperiodo = 0
if opcao == 1:
    print('\n')
    for c in range(1, mesesinvestimento + 1):
        if c == 1:
            periodo += 1
            capitalinicial = valorinvestido
            juros = capitalinicial * (taxainvmensal/100)
            capitalfinal = capitalinicial + juros
            somajuros += juros
            print('{:^10} | {:^15} | {:^10} | {:^10} | {:^15}'.format('PERÍODO','CAPITAL INICIAL','% JUROS','VLR JUROS','CAPITAL FINAL'))
            print('{:^10} | {:^15} | {:^10} | {:^10} | {:^15}'.format(periodo,round(capitalinicial,2),round(taxainvmensal,2),round(juros,2),round(capitalfinal,2)))
        else:
            periodo += 1
            capitalinicial = capitalfinal
            juros = capitalinicial * (taxainvmensal/100)
            capitalfinal = capitalinicial + juros
            somajuros += juros
            print('{:^10} | {:^15} | {:^10} | {:^10} | {:^15}'.format(periodo,round(capitalinicial,2),round(taxainvmensal,2),round(juros,2),round(capitalfinal,2)))
    print('\nO valor final do investimento será de R${}'.format(round(capitalfinal,2)))
    print('O valor acumulado de juros será de R${}'.format(round(somajuros,2)))

if opcao == 2:
    periodo = 1
    while capitalfinal < metainvestimento:
        if periodo == 1:
            capitalinicial = valorinvestido
            juros = capitalinicial * (taxainvmensal/100)
            capitalfinal = capitalinicial + juros
            somajuros += juros
            print('{:^10} | {:^15} | {:^10} | {:^10} | {:^15}'.format('PERÍODO','CAPITAL INICIAL','% JUROS','VLR JUROS','CAPITAL FINAL'))
            print('{:^10} | {:^15} | {:^10} | {:^10} | {:^15}'.format(periodo,round(capitalinicial,2),round(taxainvmensal,2),round(juros,2),round(capitalfinal,2)))
            qtdeperiodo += 1
            periodo += 1
        else:
            capitalinicial = capitalfinal
            juros = capitalinicial * (taxainvmensal/100)
            capitalfinal = capitalinicial + juros
            somajuros += juros
            print('{:^10} | {:^15} | {:^10} | {:^10} | {:^15}'.format(periodo,round(capitalinicial,2),round(taxainvmensal,2),round(juros,2),round(capitalfinal,2)))
            qtdeperiodo += 1
            periodo += 1
    print('\nO valor final do investimento será de R${}'.format(round(capitalfinal,2)))
    print('O valor acumulado de juros será de R${}'.format(round(somajuros,2)))
    print('Você levará {} meses ({} anos) para chegar ao valor final desejado'.format(qtdeperiodo,round((qtdeperiodo/12),1)))
