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
def mostra_tabuleiro(tabuleiro,linha,colunas): #mostra o tabuleiro na tela
    for i in range(linha):
        for j in range(colunas):
            print(tabuleiro[i][j],"\t", end =" ")
        print("\n")
def movimenta_jogador(direcao, tabuleiro):
    found=0 # verificação de encontro, pois encontrei um problema em que o personagem era movido e encontrado novamente depois quando ia para baixo ou para a direita
    for linha in range(len(tabuleiro)): #percorre as linha do tabuleiro
        #print("Iteração %d"%linha)
        for coluna in range(len(tabuleiro[linha])): #percorre as colunas do tabuleiro
            #print("Iteração %d %d"%(linha,coluna))
            if (tabuleiro[linha][coluna])=='Jogador' and found==0: # quando a posição no tabuleiro for o jogador e esse não tiver sido encontrado ainda
                #print("Achei o jogador em %d %d"%(linha,coluna))
                if(direcao=='w'):
                    if(linha==0):
                        print("Impossível movimentar para cima!!")
                        found=1
                    else:
                        if(verifica_posicao(tabuleiro[linha-1][coluna])==True):
                            tabuleiro[linha][coluna]=None
                            tabuleiro[linha-1][coluna]="Jogador"
                        else:
                            return False # o jogo acabou
                        found=1
                elif(direcao=='s'):
                    if(linha==len(tabuleiro)-1):
                        print("Impossível movimentar para baixo!!")
                        found=1
                    else:
                        if(verifica_posicao(tabuleiro[linha+1][coluna])==True):
                            tabuleiro[linha][coluna]=None
                            tabuleiro[linha+1][coluna]="Jogador"
                        else:
                            return False # o jogo acabou
                        found=1
                if(direcao=='a'):
                    if(coluna==0):
                        print("Impossível movimentar para a esquerda!!")
                        found=1
                    else:
                        if(verifica_posicao(tabuleiro[linha][coluna-1])==True):
                            tabuleiro[linha][coluna]=None
                            tabuleiro[linha][coluna-1]="Jogador"
                        else:
                            return False # o jogo acabou
                        found=1
                elif(direcao=='d'):
                    if(coluna==len(tabuleiro[linha])-1):
                        print("Impossível movimentar para a direita!!")
                        found=1
                    else:  
                        if(verifica_posicao(tabuleiro[linha][coluna+1])==True):
                            tabuleiro[linha][coluna]=None
                            tabuleiro[linha][coluna+1]="Jogador"
                        else:
                            return False # o jogo acabou
                        found=1
    return True # o jogador não foi engolido ou caiu num abismo
def atira_flecha(direcao,tabuleiro):
    for linha in range(len(tabuleiro)): #percorre as linha do tabuleiro
        for coluna in range(len(tabuleiro[linha])): #percorre as colunas do tabuleiro
            if (tabuleiro[linha][coluna])=='Jogador': # quando a posição no tabuleiro for o jogador, atira a flecha a partir dele
                if(direcao)=='w': #atira pra cima
                    if linha == 0:
                        print("Você atirou na parede? Você é louco!")
                    else:
                        for i in range(1,linha+1):
                            if(verifica_posicao(tabuleiro[linha-i][coluna])==True):
                                if(tabuleiro[linha-i][coluna]!="Ouro"):
                                    tabuleiro[linha-i][coluna]="Flecha"
                            elif(tabuleiro[linha-i][coluna]=="Wumpus"):
                                tabuleiro[linha-i][coluna]=None #Remove o Wumpus do jogo
                                print("Você matou o Wumpus!!!")
                                break
                            else:
                                break
                if(direcao)=='s': #atira pra baixo
                    if linha == len(tabuleiro)-1:
                        print("Você atirou na parede? Você é louco!")
                    else:
                        for i in range(1,len(tabuleiro)-linha):
                            if(verifica_posicao(tabuleiro[linha+i][coluna])==True):
                                if(tabuleiro[linha+i][coluna]!="Ouro"):
                                    tabuleiro[linha+i][coluna]="Flecha"
                            elif(tabuleiro[linha+i][coluna]=="Wumpus"):
                                tabuleiro[linha+i][coluna]=None #Remove o Wumpus do jogo
                                print("Você matou o Wumpus!!!")
                                break
                            else:
                                break
                if(direcao)=='a': #atira pra esquerda
                    if coluna == 0:
                        print("Você atirou na parede? Você é louco!")
                    else:
                        for i in range(1,coluna+1):
                            if(verifica_posicao(tabuleiro[linha][coluna-i])==True):
                                if(tabuleiro[linha][coluna-i]!="Ouro"):
                                    tabuleiro[linha][coluna-i]="Flecha"
                            elif(tabuleiro[linha][coluna-i]=="Wumpus"):
                                tabuleiro[linha][coluna-i]=None #Remove o Wumpus do jogo
                                print("Você matou o Wumpus!!!")
                                break
                            else:
                                break
                if(direcao)=='d': #atira pra direita
                    if coluna == len(tabuleiro[linha])-1:
                        print("Você atirou na parede? Você é louco!")
                    else:
                        for i in range(1,len(tabuleiro[linha])-coluna):
                            if(verifica_posicao(tabuleiro[linha][coluna+i])==True):
                                if(tabuleiro[linha][coluna+i]!="Ouro"):
                                    tabuleiro[linha][coluna+i]="Flecha"
                            elif(tabuleiro[linha][coluna+i]=="Wumpus"):
                                tabuleiro[linha][coluna+i]=None #Remove o Wumpus do jogo
                                print("Você matou o Wumpus!!!")
                                break
                            else:
                                break
                remove_flechas(tabuleiro) #Remove as "flechas" que ficaram pelo caminho no tabuleiro
def remove_flechas(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna]=="Flecha":
                tabuleiro[linha][coluna]=None
def inicia_jogo():
    tabuleiro=[]
    linhas=int(input("Com quantas linha deseja jogar?"))
    colunas=int(input("Com quantas colunas você deseja jogar?"))
    for i in range(linhas):
        tabuleiro.append([None]*colunas)
    tabuleiro[3][0]="Jogador" #jogador começa na posição [0][0]
    inserir_posicao_aleatoria("Wumpus",tabuleiro,linhas,colunas) #Wumpus em posição aleatória
    inserir_posicao_aleatoria("Ouro",tabuleiro,linhas,colunas) #Ouro em posição aleatória
    for i in range(((linhas*colunas)//5)):
        inserir_posicao_aleatoria("Abismo",tabuleiro,linhas,colunas)
    return tabuleiro
def acao_jogador(tabuleiro):
    linhas=len(tabuleiro)
    colunas=len(tabuleiro[0])
    status = True #o jogador está vivo
    flecha = True #o jogador possui uma flecha
    mostra_tabuleiro(tabuleiro,linhas,colunas) # Mostra o tabuleiro
    while status: # enquanto o jogador estiver vivo
        acao=input("Qual a próxima ação do personagem?W-A-S-D-Flecha\n")
        if acao=="Flecha" and flecha==True:
            direcao_flecha=input("Qual a direção da flecha?")
            atira_flecha(direcao_flecha,tabuleiro)
            flecha=False
            status=True
        elif(acao=='w' or acao=='s' or acao=='a' or acao=='d'):
            status = movimenta_jogador(acao,tabuleiro) #movimenta o jogador no tabuleiro e retorna se ele continua vivo
        elif flecha==False:
            print("Você não possui mais flechas!")
        mostra_tabuleiro(tabuleiro,linhas,colunas)
        #print(status)
    print('O jogo acabou')
tabuleiro = inicia_jogo()
acao_jogador(tabuleiro)
print("Qual seu nome?")
nome=input()