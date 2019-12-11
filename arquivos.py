def ler_arquivo(arquivo):
    result=[]
    arq_tab=open(arquivo,'r')
    tabuleiro=arq_tab.readlines()
    for i in range(len(tabuleiro)):
        result+=[tabuleiro[i].split(' ')]
        del result[i][-1] #remove o \n do final da lista
    arq_tab.close()
    return list(result)
def escrever_arquivo(tabuleiro,arquivo):
    arq_tab=open(arquivo,'w')
    texto=''
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            texto+=str(tabuleiro[i][j])+' '
        texto+='\n'
    arq_tab.write(texto)
    arq_tab.close()