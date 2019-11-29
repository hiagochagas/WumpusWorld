import random
def verifica_posicao(posicao_desejada): #verifica se é um abismo ou Wumpus
    if(posicao_desejada=="Wumpus" or posicao_desejada=="Abismo"):
        #print("O jogo acabou")
        return False # não é seguro
    else:
        return True #é seguro
def inserir_posicao_aleatoria(elemento,tabuleiro,x_maximo,y_maximo): #insere um elemento numa posição aleatória, Wumpus, Abismo e Ouro
    x=random.randrange(0,x_maximo)
    y=random.randrange(0,y_maximo)
    #print(x,y)
    if tabuleiro[x][y]==None:    
        tabuleiro[x][y]=elemento
    else:
        inserir_posicao_aleatoria(elemento,tabuleiro,x_maximo,y_maximo)
def mostra_tabuleiro(tabuleiro,linhas,colunas): #mostra o tabuleiro na tela
    for i in range(linhas):
        for j in range(colunas):
            print(tabuleiro[i][j],"\t", end =" ")
        print("\n")
def movimenta_jogador(direcao, tabuleiro):
    found=0 # verificação de encontro, pois encontrei um problema em que o personagem era movido e encontrado novamente depois quando ia para baixo ou para a direita
    for i in range(len(tabuleiro)): #percorre as linhas do tabuleiro
        #print("Iteração %d"%i)
        for j in range(len(tabuleiro[i])): #percorre as colunas do tabuleiro
            #print("Iteração %d %d"%(i,j))
            if (tabuleiro[i][j])=='Jogador' and found==0: # quando a posição no tabuleiro for o jogador e esse não tiver sido encontrado ainda
                #print("Achei o jogador em %d %d"%(i,j))
                if(direcao=='w'):
                    if(i==0):
                        print("Impossível movimentar para cima!!")
                        found=1
                    else:
                        if(verifica_posicao(tabuleiro[i-1][j])==True):
                            tabuleiro[i][j]=None
                            tabuleiro[i-1][j]="Jogador"
                        else:
                            return False # o jogo acabou
                        found=1
                elif(direcao=='s'):
                    if(i==len(tabuleiro)-1):
                        print("Impossível movimentar para baixo!!")
                        found=1
                    else:
                        if(verifica_posicao(tabuleiro[i+1][j])==True):
                            tabuleiro[i][j]=None
                            tabuleiro[i+1][j]="Jogador"
                        else:
                            return False # o jogo acabou
                        found=1
                if(direcao=='a'):
                    if(j==0):
                        print("Impossível movimentar para a esquerda!!")
                        found=1
                    else:
                        if(verifica_posicao(tabuleiro[i][j-1])==True):
                            tabuleiro[i][j]=None
                            tabuleiro[i][j-1]="Jogador"
                        else:
                            return False # o jogo acabou
                        found=1
                elif(direcao=='d'):
                    if(j==len(tabuleiro[i])-1):
                        print("Impossível movimentar para a direita!!")
                        found=1
                    else:  
                        if(verifica_posicao(tabuleiro[i][j+1])==True):
                            tabuleiro[i][j]=None
                            tabuleiro[i][j+1]="Jogador"
                        else:
                            return False # o jogo acabou
                        found=1
    return True # o jogador não foi engolido ou caiu num abismo
def inicia_jogo():
    tabuleiro=[]
    linhas=int(input("Com quantas linhas deseja jogar?"))
    colunas=int(input("Com quantas colunas você deseja jogar?"))
    for i in range(linhas):
        tabuleiro.append([None]*colunas)
    tabuleiro[linhas-1][0]="Jogador"
    inserir_posicao_aleatoria("Wumpus",tabuleiro,linhas,colunas)
    inserir_posicao_aleatoria("Ouro",tabuleiro,linhas,colunas)
    for i in range(((linhas*colunas)//5)):
        inserir_posicao_aleatoria("Abismo",tabuleiro,linhas,colunas)
    mostra_tabuleiro(tabuleiro,linhas,colunas)
    status = True
    while status:
        movimento=input("Qual a próxima ação do personagem?W-A-S-D\n")
        status = movimenta_jogador(movimento,tabuleiro)
        mostra_tabuleiro(tabuleiro,linhas,colunas)
        print(status)
    print('O jogo acabou')
inicia_jogo()
print("Qual seu nome?")
nome=input()