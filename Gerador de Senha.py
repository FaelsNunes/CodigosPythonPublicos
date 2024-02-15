from random import shuffle #Importa o embaralhador

#Imprime o título do programa
print('-=-' * 10)
titulo = 'GERADOR DE SENHA'
print('{:^30}'.format(titulo))
print('-=-' * 10)

#Pergunta o tamanho da senha
qtdecaract = int(input('Qual o tamanho da senha? '))

#Cria a lista com os cacacteres disponíveis para a senha
caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','w','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','W','Z','!','@','#','$','%','&','*','(',')','+','=','-','[',']','{','}','?','.',',','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','&','*','(',')','+','=','-','[',']','{','}','?','.',',','0','1','2','3','4','5','6','7','8','9']

shuffle(caracteres) #Embaralha a lista
senha = (caracteres[0:qtdecaract]) #Pega os primeiros caracteres da lista, conforme o máximo definido pelo usuário
senha = ''.join(senha) #Faz a junção dos caracteres sem espaço algum entre eles
#Imprime o resultado
print('\nSENHA GERADA COM SUCESSO!\n')
print(senha)