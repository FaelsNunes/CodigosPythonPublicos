import tkinter as tki

#define uma função
def Somar():
    n1 = int(texto1.get())
    n2 = int(texto2.get())
    #print(n1+n2) #Mostra o resultado internamente para mim
    mostrarresultado['text'] = n1+n2


telalogin = tki.Tk() #Iníncio da página (Instância de Tk)
telalogin.geometry('800x400') #Define o tamanho da tela
telalogin.title('Tela de Cadastro') #Define o titulo da janela

texto1 = tki.Entry() #Cria um campo de texto
texto1.grid(row=0, column=0) #coloca ele na linha 0 e coluna 0 da janeja

texto2 = tki.Entry()  #Cria um campo de texto
texto2.grid(row=1, column=0)  #coloca ele na linha 1 e coluna 0 da janeja

botao1 = tki.Button(text='SOMAR', command=Somar) #Cria um botão, executa a função somar
botao1.grid(row=2, column=0) #coloca ele na linha 2 e coluna 0 da janeja
#Se colcoar a função -> Somar() O python tenta executar ela de cara
#Se colcoar a função -> Somar O python executa ela quando é clicado no botão

mostrarresultado = tki.Label(text='RESULTADO') #Cria uma label com o texto chamado resultado
mostrarresultado.grid(row=3, column=0)

telalogin.mainloop() #Fim da página