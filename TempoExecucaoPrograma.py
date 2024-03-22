'''
Programa destinado a ser copiado para outros programas para poder mostrar o tempo de execução
Está puxando as funções do meu pacote, por via das dúvidas estou incluind abaixo as duas funções aqui
'''
from FuncoesRnb import dates, strings

'''
def data_hora_atual():
    import datetime
    agora = datetime.datetime.now() #pega a data e hora atual
    agora = datetime.datetime(agora.year,agora.month,agora.day,agora.hour,agora.minute,agora.second)
    return agora
    
##########################################################################################################

def titulo(msg):
    print('-=' * ((len(msg) // 2) + 2))
    print('  {:^}'.format(msg))
    print('-=' * ((len(msg) // 2) + 2))


'''

inicioexecucao = dates.data_hora_atual()

'''
Escrever o programa aqui
'''

fimexecucao = dates.data_hora_atual()
tempoexecucao = (fimexecucao - inicioexecucao)
print('\n')
strings.titulo('DETALHES DA EXECUÇÃO')
print(f'Início da execução: {inicioexecucao}')
print(f'Fim da execução: {fimexecucao}')
print(f'Duração da execução: {tempoexecucao}')
print('\n')
