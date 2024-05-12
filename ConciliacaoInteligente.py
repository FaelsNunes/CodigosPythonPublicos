#OBSERVAÇÃO
#Inserindo 20 valores já teremos analisados 1.048.575 combinações
#A cada inserção a quantidade de combinações sobe exponencialmente
#Não é possível colocar muito mais do que isso se não trava o programa

from itertools import combinations

valorProcurado = 20 #Inserir o valor aqui, exemplo: 156.78

#Inserir os valores abaixo, exemplo: 1.95,2.35
valores = []
qtdePosicoes = len(valores)

combinacoes = []
combinacoesPossiveis = []
qtdeCombinacoes = 0
qtdeCombSucesso = 0

print(f'Meta: Procurar todas as combinações possíveis que a soma dos valores seja igual a {valorProcurado}\n')

for a in range(1,qtdePosicoes + 1):
    combinacoes = list(combinations(valores,a))
    combinacoesPossiveis.append(combinacoes)

for C,I in enumerate(combinacoesPossiveis):
    for c,v in enumerate(I):
        qtdeCombinacoes += 1
        if round(sum(v),2) == valorProcurado:
            print(f'{v} -> Soma: {round(sum(v),2)}')
            qtdeCombSucesso += 1

print(f'\nForam avaliadas {qtdeCombinacoes} combinações possíveis, {qtdeCombSucesso} combinação(ões) atendeu(ram) ao resultado procurado.')
if qtdeCombSucesso > 0:
    print('Você pode retirar estes valores da lista original para poder procurar novas metas dentro dos números que sobraram.')
