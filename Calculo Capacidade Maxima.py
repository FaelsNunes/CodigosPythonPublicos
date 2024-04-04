valorTotal = str(input('Qual o valor/volume/quantidade total? ')).strip()
valorTotal = float(valorTotal.replace(',','.').replace('%','').replace('R$','').replace('$','').replace(' ',''))

valorUnidade = str(input('Qual o valor/volume/quantidade unitário? ')).strip()
valorUnidade = float(valorUnidade.replace(',','.').replace('%','').replace('R$','').replace('$','').replace(' ',''))

unidade = 0
soma = 0
saldo = valorTotal

while True:
    soma += valorUnidade
    if soma > valorTotal:
        break
    else:
        saldo -= valorUnidade
        unidade += 1

print(f'\nCapacidade de {unidade} unidades e sobra {round(saldo,2)} do valor/volume/quantidade total')
