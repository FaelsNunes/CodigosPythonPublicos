import unicodedata

palavras = []
qtdpalavras = len(palavras) + 0
processamento = ''

decespaco = 'F'
while decespaco not in ('SN'):
    decespaco = str(input('Você quer remover espaços? [S/N] ')).upper()[0]

decespcaract = 'F'
while decespcaract not in ('SN'):
    decespcaract = str(input('Você quer remover caracteres especiais? [S/N] ')).upper()[0]

decminusculas = 'F'
while decminusculas not in ('SN'):
    decminusculas = str(input('Você quer que todas as letras fiquem minúsculas? [S/N] ')).upper()[0]

print('\n')

for c in range (0, qtdpalavras):
    processamento = unicodedata.normalize("NFD", palavras[c].strip())
    processamento = processamento.encode("ascii", "ignore")
    processamento = processamento.decode("utf-8")
    if decespaco == 'S':
        processamento = processamento.replace(' ','')
    if decespcaract == 'S':
        processamento = processamento.replace('"','').replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('¨','').replace('&','').replace('*','').replace('(','').replace(')','').replace('_','').replace('-','').replace('+','').replace('=','').replace('§','').replace('/','').replace('?','').replace('°','').replace('´','').replace('`','').replace('[','').replace('{','').replace('ª','').replace('^','').replace('~','').replace(']','').replace('}','').replace('º','').replace('|','').replace(',','').replace('<','').replace('.','').replace('>','').replace(';','').replace(':','')
    if decminusculas == 'S':
        processamento = processamento.lower()
    print(processamento)
