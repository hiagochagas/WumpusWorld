import random
import arquivos
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
def fedor_e_brisa(tabuleiro): #detecta fedor e brisa a partir da posição do jogador no tabuleiro
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna]=="Jogador":
                if(linha>0 and linha<len(tabuleiro)-1 and coluna>0 and coluna<len(tabuleiro[linha])-1): #parte central do tabuleiro
                    if(tabuleiro[linha-1][coluna]=="Wumpus" or tabuleiro[linha+1][coluna]=="Wumpus" or tabuleiro[linha][coluna-1]=="Wumpus" or tabuleiro[linha][coluna+1]=="Wumpus"):
                        print("Você sente um fedor intenso.")
                    if(tabuleiro[linha-1][coluna]=="Abismo" or tabuleiro[linha+1][coluna]=="Abismo" or tabuleiro[linha][coluna-1]=="Abismo" or tabuleiro[linha][coluna+1]=="Abismo"):
                        print("Você sente uma brisa atravessar o seu corpo.")
                elif linha==0 and coluna==0: #porta superior esquerda
                    if(tabuleiro[linha+1][coluna]=="Wumpus" or tabuleiro[linha][coluna+1]=="Wumpus"):
                        print("Você sente um fedor intenso.")
                    if(tabuleiro[linha+1][coluna]=="Abismo" or tabuleiro[linha][coluna+1]=="Abismo"):
                        print("Você sente uma brisa atravessar o seu corpo.")
                elif linha==0 and coluna==len(tabuleiro[linha])-1: #ponta superior direita
                    if(tabuleiro[linha+1][coluna]=="Wumpus" or tabuleiro[linha][coluna-1]=="Wumpus"):
                        print("Você sente um fedor intenso.")
                    if(tabuleiro[linha+1][coluna]=="Abismo" or tabuleiro[linha][coluna-1]=="Abismo"):
                        print("Você sente uma brisa atravessar o seu corpo.")
                elif linha==len(tabuleiro)-1 and coluna==0: #ponta inferior esquerda
                    if(tabuleiro[linha-1][coluna]=="Wumpus" or tabuleiro[linha][coluna+1]=="Wumpus"):
                        print("Você sente um fedor intenso.")
                    if(tabuleiro[linha-1][coluna]=="Abismo" or tabuleiro[linha][coluna+1]=="Abismo"):
                        print("Você sente uma brisa atravessar o seu corpo.")
                elif linha==len(tabuleiro)-1 and coluna==len(tabuleiro[linha])-1: #ponta inferior direita
                    if(tabuleiro[linha-1][coluna]=="Wumpus" or tabuleiro[linha][coluna-1]=="Wumpus"):
                        print("Você sente um fedor intenso.")
                    if(tabuleiro[linha-1][coluna]=="Abismo" or tabuleiro[linha][coluna-1]=="Abismo"):
                        print("Você sente uma brisa atravessar o seu corpo.")
                elif linha==0: #parte superior
                    if(tabuleiro[linha+1][coluna]=="Wumpus" or tabuleiro[linha][coluna-1]=="Wumpus" or tabuleiro[linha][coluna+1]=="Wumpus"):
                        print("Você sente um fedor intenso.")
                    if(tabuleiro[linha+1][coluna]=="Abismo" or tabuleiro[linha][coluna-1]=="Abismo" or tabuleiro[linha][coluna+1]=="Abismo"):
                        print("Você sente uma brisa atravessar o seu corpo.")
                elif coluna==0: #coluna da esquerda
                    if(tabuleiro[linha-1][coluna]=="Wumpus" or tabuleiro[linha+1][coluna]=="Wumpus" or tabuleiro[linha][coluna+1]=="Wumpus"):
                        print("Você sente um fedor intenso.")
                    if(tabuleiro[linha-1][coluna]=="Abismo" or tabuleiro[linha+1][coluna]=="Abismo" or tabuleiro[linha][coluna+1]=="Abismo"):
                        print("Você sente uma brisa atravessar o seu corpo.")
                elif linha==len(tabuleiro)-1: #linha inferior
                    if(tabuleiro[linha-1][coluna]=="Wumpus" or tabuleiro[linha][coluna-1]=="Wumpus" or tabuleiro[linha][coluna+1]=="Wumpus"):
                        print("Você sente um fedor intenso.")
                    if(tabuleiro[linha-1][coluna]=="Abismo" or tabuleiro[linha][coluna-1]=="Abismo" or tabuleiro[linha][coluna+1]=="Abismo"):
                        print("Você sente uma brisa atravessar o seu corpo.")
                elif coluna==len(tabuleiro[linha])-1: #coluna da direita
                    if(tabuleiro[linha-1][coluna]=="Wumpus" or tabuleiro[linha+1][coluna]=="Wumpus" or tabuleiro[linha][coluna-1]=="Wumpus"):
                        print("Você sente um fedor intenso.")
                    if(tabuleiro[linha-1][coluna]=="Abismo" or tabuleiro[linha+1][coluna]=="Abismo" or tabuleiro[linha][coluna-1]=="Abismo"):
                        print("Você sente uma brisa atravessar o seu corpo.")
def ouro_coletado(tabuleiro): #verifica se o Ouro ainda está em jogo
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna]=="Ouro":
                return False
    return True
def mostra_tabuleiro(tabuleiro,linha,colunas): #mostra o tabuleiro na tela
    for i in range(linha):
        for j in range(colunas):
            print(tabuleiro[i][j],"\t", end =" ")
        print("\n")
def movimenta_jogador(direcao, tabuleiro):
    found=0 # verificação de encontro, pois encontrei um problema em que o personagem era movido e encontrado novamente depois quando ia para baixo ou para a direita
    for linha in range(len(tabuleiro)): 
        for coluna in range(len(tabuleiro[linha])): 
            if (tabuleiro[linha][coluna])=='Jogador' and found==0: # quando a posição no tabuleiro for o jogador e esse não tiver sido encontrado ainda
                if(direcao=='w'):
                    if(linha==0):
                        print("Impossível movimentar para cima!!")
                        found=1
                    else:
                        if(verifica_posicao(tabuleiro[linha-1][coluna])==True):
                            tabuleiro[linha][coluna]=None
                            if(tabuleiro[linha-1][coluna]=="Ouro"):
                                print("Você nota um objeto brilhante no chão. Você capturou o Ouro!!")
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
                            if(tabuleiro[linha+1][coluna]=="Ouro"):
                                print("Você nota um objeto brilhante no chão. Você capturou o Ouro!!")
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
                            if(tabuleiro[linha][coluna-1]=="Ouro"):
                                print("Você nota um objeto brilhante no chão. Você capturou o Ouro!!")
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
                            if(tabuleiro[linha][coluna+1]=="Ouro"):
                                print("Você nota um objeto brilhante no chão. Você capturou o Ouro!!")
                            tabuleiro[linha][coluna+1]="Jogador"
                        else:
                            return False # o jogo acabou
                        found=1
    return True # o jogador não foi engolido ou caiu num abismo
def atira_flecha(direcao,tabuleiro,pontuacao):
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
                                pontuacao+=10000
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
                                pontuacao+=10000
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
                                pontuacao+=10000
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
                                pontuacao+=10000
                                break
                            else:
                                break
                remove_flechas(tabuleiro) #Remove as "flechas" que ficaram pelo caminho no tabuleiro
    return pontuacao
def remove_flechas(tabuleiro):
    for linha in range(len(tabuleiro)):
        for coluna in range(len(tabuleiro[linha])):
            if tabuleiro[linha][coluna]=="Flecha":
                tabuleiro[linha][coluna]=None
def inicia_jogo_novo(pontuacao):
    tabuleiro=[]
    linhas=int(input("Com quantas linha deseja jogar?"))
    colunas=int(input("Com quantas colunas você deseja jogar?"))
    for i in range(linhas):
        tabuleiro.append([None]*colunas)
    tabuleiro[0][0]="Jogador" #jogador começa na posição [0][0]
    inserir_posicao_aleatoria("Wumpus",tabuleiro,linhas,colunas) #Wumpus em posição aleatória
    inserir_posicao_aleatoria("Ouro",tabuleiro,linhas,colunas) #Ouro em posição aleatória
    for i in range(((linhas*colunas)//5)):
        inserir_posicao_aleatoria("Abismo",tabuleiro,linhas,colunas)
    acao_jogador(tabuleiro,pontuacao)
def acao_jogador(tabuleiro,pontuacao):
    linhas=len(tabuleiro)
    colunas=len(tabuleiro[0])
    status = True #o jogador está vivo
    flecha = True #o jogador possui uma flecha
    mostra_tabuleiro(tabuleiro,linhas,colunas) # Mostra o tabuleiro
    fedor_e_brisa(tabuleiro)
    while status: # enquanto o jogador estiver vivo
        acao=input("Qual a próxima ação do personagem?W-A-S-D-Flecha\n")
        if acao=="Flecha" and flecha==True:
            direcao_flecha=input("Qual a direção da flecha?")
            pontuacao=atira_flecha(direcao_flecha,tabuleiro,pontuacao)
            flecha=False
        elif(acao=='w' or acao=='s' or acao=='a' or acao=='d'):
            status = movimenta_jogador(acao,tabuleiro) #movimenta o jogador no tabuleiro e retorna se ele continua vivo
            pontuacao-=1
            if(ouro_coletado):
                pontuacao+=1000
        elif flecha==False:
            print("Você não possui mais flechas!")
        if(tabuleiro[0][0]=="Jogador" and ouro_coletado(tabuleiro)==True):
            pontuacao+=100
            break
        fedor_e_brisa(tabuleiro)
        mostra_tabuleiro(tabuleiro,linhas,colunas)
        arquivos.escrever_arquivo(tabuleiro,'tabuleiro.txt')
    if(status==False):
        pontuacao-=10000#pontuação por morte
    print('O jogo acabou')
    arquivos.escrever_arquivo('','tabuleiro.txt')#salva um jogo vazio
    escolha=int(input("Deseja jogar novamente?"))
    if(escolha==1):    
        inicia_jogo_novo(pontuacao)
    else:
        print("Sua pontuação: %d"%pontuacao)
        nome=input("Qual seu nome?")
def bem_vindo():    
    print("Seja bem vindo ao Wumpus World:")
    print("Deseja criar um novo tabuleiro ou continuar de onde parou?\n1-Criar um novo\n2-Continuar")
    escolha=int(input())
    if escolha==1:    
        inicia_jogo_novo(0)
    elif escolha==2:
        try:
            tabuleiro=arquivos.ler_arquivo('tabuleiro.txt')
            acao_jogador(tabuleiro,0)
        except:
            print("Você não possui jogo salvo")
            bem_vindo()
bem_vindo()