print('-=-' * 30) #Faz uma quebra de página
print('QUAL OPÇÃO DE CÁLCULO DE PERCENTUAL VOCÊ QUER UTILIZAR?')
print('-=-' * 30) #Faz uma quebra de página

#Estabelece as opções disponíveis ao usuário
print('\n1 - 10/100 é igual a 10%.\n2 - 10% de 100 corresponde a 10.\n3 - 10 corresponde a 10% de 100.')

#Registra a opção escolhida pelo usuário
opcaousuario = int(input('\nDigite o número da opção escolhida: '.upper()))

#Recebe o primeiro valor se a opção escolhida for 1
if opcaousuario	== 1:
	n1 = str(input('\nDigite o número que você quer dividir: ')).strip() #Recebe o valor como texto
	n1 = float(n1.replace(',','.')) #Altera a virgula para ponto e altera o valor para float

#Recebe o segundo valor se a opção escolhida for 1
if opcaousuario	== 1:
	n2 = str(input('Digite o número que será a base da divisão: ')).strip() #Recebe o valor como texto
	n2 = float(n2.replace(',','.')) #Altera a virgula para ponto e altera o valor para float

#Recebe o primeiro valor se a opção escolhida for 2
if opcaousuario	== 2:
	n1 = str(input('\nDigite o % que você quer descobrir o valor: ')).strip() #Recebe o valor como texto
	n1 = float(n1.replace(',','.').replace('%','')) #Altera a virgula para ponto, % para nada, e altera o valor para float

#Recebe o segundo valor se a opção escolhida for 2
if opcaousuario	== 2:
	n2 = str(input('Digite o número que será a base para descobrir o valor: ')).strip() #Recebe o valor como texto
	n2 = float(n2.replace(',','.')) #Altera a virgula para ponto e altera o valor para float

#Recebe o primeiro valor se a opção escolhida for 3
if opcaousuario	== 3:
	n1 = str(input('\nDigite o número que você tem: ')).strip() #Recebe o valor como texto
	n1 = float(n1.replace(',','.')) #Altera a virgula para ponto e altera o valor para float

#Recebe o segundo valor se a opção escolhida for 3
if opcaousuario	== 3:
	n2 = str(input('Digite o % que este número corresponde: ')).strip() #Recebe o valor como texto
	n2 = float(n2.replace(',','.').replace('%','')) #Altera a virgula para ponto, % para nada, e altera o valor para float

print('\n') #Dá um espaço na tela

#Se a opção escolhida for inválida, exibe mensagem na tela
if opcaousuario > 3 or opcaousuario <= 0:
	print('Opção escolhida não é valida!'.upper())

#Faz o cálculo se a opção escolhida for 1
if opcaousuario == 1:
	R = (n1/n2)*100

#Faz o cálculo se a opção escolhida for 2
if opcaousuario == 2:
	R = (n2*(n1/100))

#Faz o cálculo se a opção escolhida for 3
if opcaousuario == 3:
	R = (n1/(n2/100))

#Resultado se a opção escolhida for 1
if opcaousuario == 1:
	print('{}/{} é igual a {}%'.format(str(n1).replace('.',','),str(n2).replace('.',','),str(round(R,1)).replace('.',',')))

#Resultado se a opção escolhida for 2
if opcaousuario == 2:
	print('{}% de {} é igual a {}'.format(str(n1).replace('.',','),str(n2).replace('.',','),str(round(R,1)).replace('.',',')))

#Resultado se a opção escolhida for 3
if opcaousuario == 3:
	print('{} corresponde a {}% de {}'.format(str(n1).replace('.',','),str(n2).replace('.',','),str(round(R,1)).replace('.',',')))

print('\n') #Dá um espaço na tela

print('-=-' * 30) #Faz uma quebra de página

'''

#ORIGINAL

print('Quantos % este número é de outro número?')
n1 = str(input('Digite o número que você quer saber o percentual: (Ex. 10,5) ')).strip()
n1 = float(n1.replace(',','.'))
n2 = str(input('Digite o número que será a base para ser encontrado o percentual: (Ex. 101,80) ')).strip()
n2 = float(n2.replace(',','.'))
p1 = n1/n2
print('O que você quer saber é: \nQual percentual {} é de {}?'.format(str(n1).replace('.',','),str(n2).replace('.',',')))
print('Se foi essa sua dúvida o resultado é: {}%'.format(str(round(p1*100,2)).replace('.',',')))
print('Caso seja a sua dúvida mas os números estão invertidos, inicialize o programa novamente')
print('Caso não seja sua dúvida, veja a próxima solução\n',)

print('Este número vezes X% da quanto?')
n3 = str(input('Digite o número que é a base do cálculo: ')).strip()
n3 = float(n3.replace(',','.'))
p2 = str(input('Digite o percentual que será calculado: ')).strip()
p2 = float(p2.replace(',','.').replace('%',''))
n4 = n3*(p2/100)
print('O que você quer saber é: \n{} vezes {}% da quanto?'.format(n3,p2))
#print('Se foi essa sua dúvida o resultado é: {:.2f}'.format(n4))
print('Se foi essa sua dúvida o resultado é: {}'.format(str(n4).replace('.',',')))
print('Caso seja a sua dúvida mas os números estão invertidos, inicialize o programa novamente')
print('Caso não seja sua dúvida, veja a próxima solução\n')

print('Este número dividido por X% da quanto?')
n5 = str(input('Digite o número que você quer dividir: ')).strip()
n5 = float(n5.replace(',','.'))
p3 = str(input('Digite o percentual que será dividido: ')).strip()
p3 = float(p3.replace(',','.').replace('%',''))
n6 = n5/(p3/100)
print('O que você quer saber é: \n{} é {}% de quanto?'.format(n5,p3))
print('Se foi essa sua dúvida o resultado é: {}'.format(str(round(n6,2)).replace('.',',')))
print('Caso seja a sua dúvida mas os números estão invertidos, inicialize o programa novamente')
print('Caso não seja sua dúvida, veja a próxima solução\n')
'''