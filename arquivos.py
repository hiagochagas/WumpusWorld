def ler_arquivo(arquivo):
    try:
        result=[]
        arq_tab=open(arquivo,'r')
        matriz=arq_tab.readlines()
        for i in range(len(matriz)):
            result+=[matriz[i].split(' ')]
            del result[i][-1] #remove o \n do final da lista
        arq_tab.close()
        return list(result)
    except:
        print("NÃO HÁ NADA NO ARQUIVO")
def escrever_arquivo(matriz,arquivo):
    arq_tab=open(arquivo,'w')
    texto=''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            texto+=str(matriz[i][j])+' '
        texto+='\n'
    arq_tab.write(texto)
    arq_tab.close()