import random
import time
from colorama import Fore, Back, Style
#variaveis

#IDE RECOMENDOU PQ SE N DAVA PAU
matrizJUmUm: list=[]
matrizJUmDois: list=[]
matrizJDoisUm: list=[]
matrizJDoisDois: list=[]
#funções
def menu_inicial():
    print(Fore.BLUE + 25 * "-")
    print(Fore.LIGHTWHITE_EX + "Escolha o seu modo de jogo")
    print("1 - Jogar contra a máquina")
    print("2 - Jogar no modo PvP")
    print(Fore.BLUE + 25 * "-")

    modoJogo=input(Fore.LIGHTWHITE_EX + "Sua escolha: ")
    print(Fore.BLUE + 25 * "-")
    #verificador pra ver se a resposta está correta
    while modoJogo not in("1","2"):
        modoJogo = input(Fore.LIGHTWHITE_EX + "Escolha entre o modo 1 e o modo 2: ")
        print(Fore.BLUE + 25 * "-")
    #escolha nome
    if modoJogo=="1":
        nomeJUm=input(Fore.LIGHTWHITE_EX + "Digite o seu nome jogador: ")
        print(Fore.BLUE + 25 * "-")
        nomeJDois="máquina"
    else:
        nomeJUm=input(Fore.LIGHTWHITE_EX + "Digite o seu nome jogador 1: ")
        nomeJDois=input(Fore.LIGHTWHITE_EX + "Digite o seu nome jogador 2: ")
        print(Fore.BLUE + 25 * "-")

    return modoJogo, nomeJUm,nomeJDois

def configurar_tabuleiro():
    #para criar as matrizes
    tamanho = input(Fore.LIGHTWHITE_EX + "Digite o tamanho do tabuleiro entre 10 e 20: ")
    print(Fore.BLUE + 50 * "-")
    #tive q usar o try pq com o if n tava rolando, peguei de um stack overflow de java kkkkkkk
    try:
        tamanho = int(tamanho)
    except ValueError:
        tamanho = 0
    while 10 > int(tamanho) or int(tamanho) > 20:
        tamanho = input(Fore.LIGHTWHITE_EX + "Tamanho inválido, Escolha entre 10 e 20: ")
        try:
            tamanho = int(tamanho)
        except ValueError:
            tamanho = 0
        print(Fore.BLUE + 50 * "-")
    tamanho = int(tamanho)
    #aqui to pensando em já transformar nas 4 matrizes e passar pras proximas os params direto
    return tamanho

def posicionar_navios(gamemode,tamanho):
    #print("para permitir o posicionamento manual.")

    """
    tinha feito diferente antes, só colocar um if no final e fzr um random choice e um ngc pra n repetir
    """

    matrizJUmUm=[[Fore.BLUE+"~"]*tamanho for i in range(tamanho)]
    matrizJUmDois=[[Fore.BLUE+"~"]*tamanho for i in range(tamanho)]
    matrizJDoisUm = [[Fore.BLUE+"~"]*tamanho for i in range(tamanho)]
    matrizJDoisDois = [[Fore.BLUE+"~"]*tamanho for i in range(tamanho)]

    matrizMestre=[matrizJUmUm,matrizJUmDois,matrizJDoisUm,matrizJDoisDois]

    #fazer dicionario aqui
    letrasPNum={
          "a": 0,
          "b": 1,
          "c": 2,
          "d": 3,
          "e": 4,
          "f": 5,
          "g": 6,
          "h": 7,
          "i": 8,
          "j": 9,
          "k": 10,
          "l": 11,
          "m": 12,
          "n": 13,
          "o": 14,
          "p": 15,
          "q": 16,
          "r": 17,
          "s": 18,
          "t": 19
    }


    #criei isso pra n ter q bifurcar e repetir td
    for i in range(int(gamemode)):

        if i==0:
            x=0
        else:
            x=2

        #mostrar matriz pro player
        matriz = [[Fore.BLUE + "~"] * tamanho for i in range(tamanho)]
        # lista pra ajudar a printar as letras
        print(Fore.LIGHTWHITE_EX + "Este é o tabuleiro")
        print(Fore.BLUE + 25 * "-")
        listaPrintLetra = ["---", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                           "Q", "R", "S", "T"]
        # counter pra indicar a linha
        indicadorLinha = 1
        # isso é pra printar só os q o player indicou
        print(Fore.GREEN + " ".join(listaPrintLetra[0:tamanho + 1]) + Style.RESET_ALL, end="\n")
        # print normal e o indicador mostra qual linha
        for i in matriz:
            linha_colorida = f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL} " + " ".join(i)
            if indicadorLinha < 10:
                print(linha_colorida)
            else:
                print(f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL}{' '.join(i)}")
            indicadorLinha += 1

        #encouraçado
        print(Fore.BLUE + 50 * "-") 
        encouracadoLinha = input(Fore.LIGHTWHITE_EX + f"Digite um número de linha (1 a {len(matrizJUmUm[0])})para o encouraçado (5 casas): ")
        print(Fore.BLUE + 25 * "-")
        try:
            encouracadoLinha = int(encouracadoLinha)
        except ValueError:
            encouracadoLinha = -1
        encouracadoLinha=int(encouracadoLinha)
        while encouracadoLinha-1 >= len(matrizJUmUm[1]) or encouracadoLinha-1 < 0:
            encouracadoLinha = input(Fore.LIGHTWHITE_EX + f"linha inválida digite um número entre 1 e {len(matrizJUmUm[0])}: ")
            print(Fore.BLUE + 25 * "-")
            try:
                encouracadoLinha = int(encouracadoLinha)
            except ValueError:
                encouracadoLinha = -1
            encouracadoLinha = int(encouracadoLinha)
        encouracadoLinha-=1
        encouracadoCol = input(Fore.LIGHTWHITE_EX + "Digite uma letra para a coluna inicial: ").lower()
        print(Fore.BLUE + 25 * "-")
        while encouracadoCol not in letrasPNum or letrasPNum[encouracadoCol] > (len(matrizJUmUm[1]) - 5):
            encouracadoCol = input(Fore.LIGHTWHITE_EX +"letra inválida, digite dnv: ").lower()
            print(Fore.BLUE + 25 * "-")

        valorEncouracadoCol = letrasPNum[encouracadoCol]

        matrizMestre[x][encouracadoLinha][valorEncouracadoCol: valorEncouracadoCol + 5] = Fore.LIGHTWHITE_EX+"¬","¬","¬","¬","¬"


        # porta-aviões
        #add verificacao pra ver se repete
        repetido=True
        while repetido==True:
            portaAvioesLinha = input(Fore.LIGHTWHITE_EX + f"Digite um número de linha (1 a {len(matrizJUmUm[0])}) para o porta-avioes (4 casas): ")
            print(Fore.BLUE + 25 * "-")
            try:
                portaAvioesLinha = int(portaAvioesLinha)
            except ValueError:
                portaAvioesLinha = -1
            portaAvioesLinha = int(portaAvioesLinha)
            while portaAvioesLinha - 1 >= len(matrizJUmUm[1]) or portaAvioesLinha - 1 < 0:
                portaAvioesLinha = input(Fore.LIGHTWHITE_EX + f"linha inválida digite um número entre 1 e {len(matrizJUmUm[0])}: ")
                print(Fore.BLUE + 25 * "-")
                try:
                    portaAvioesLinha = int(portaAvioesLinha)
                except ValueError:
                    portaAvioesLinha = -1
            portaAvioesLinha -= 1
            portaAvioesCol = input(Fore.LIGHTWHITE_EX + "Digite uma letra para a coluna inicial: ").lower()
            print(Fore.BLUE + 25 * "-")
            while portaAvioesCol not in letrasPNum or letrasPNum[portaAvioesCol] > (len(matrizJUmUm[1]) - 5):
                portaAvioesCol = input(Fore.LIGHTWHITE_EX + "letra inválida, digite dnv: ").lower()
                print(Fore.BLUE + 25 * "-")

            valorPortaAvioesCol=letrasPNum[portaAvioesCol]
            #chcker pra ver se repete
            espacosLivres = 0
            for i in range(valorPortaAvioesCol, valorPortaAvioesCol + 4):
                if matrizMestre[x][portaAvioesLinha][i] == Fore.BLUE+"~":
                    espacosLivres += 1

            if espacosLivres == 4:
                repetido = False

                matrizMestre[x][portaAvioesLinha][valorPortaAvioesCol:valorPortaAvioesCol+4]=Fore.LIGHTWHITE_EX+"#","#","#","#"

        #a partir daqui so coloque for ctrl c ctrl v e mudar as var e numeros
        #2 Contratorpedeiros  com 3 casas cada
        for i in range(2):
            repetido = True
            while repetido == True:
                contraLinha =input(
                        Fore.LIGHTWHITE_EX + f"Digite um número de linha (1 a {len(matrizJUmUm[0])}) para o contratorpedeiro {i+1} (3 casas): ")
                print(Fore.BLUE + 25 * "-")
                try:
                    contraLinha = int(contraLinha)
                except ValueError:
                    contraLinha = -1
                while contraLinha - 1 >= len(matrizJUmUm[1]) or contraLinha - 1 < 0:
                    contraLinha = input(Fore.LIGHTWHITE_EX + f"linha inválida digite um número entre 1 e {len(matrizJUmUm[0])}: ")
                    print(Fore.BLUE + 25 * "-")
                    try:
                        contraLinha = int(contraLinha)
                    except ValueError:
                        contraLinha = -1
                contraLinha -= 1
                print(Fore.BLUE + 25 * "-")
                contraCol = input(Fore.LIGHTWHITE_EX + "Digite uma letra para a coluna inicial: ").lower()
                print(Fore.BLUE + 25 * "-")
                while contraCol not in letrasPNum or letrasPNum[contraCol] > (len(matrizJUmUm[1]) - 4):
                    contraCol = input(Fore.LIGHTWHITE_EX + "letra inválida, digite dnv: ").lower()
                    print(Fore.BLUE + 25 * "-")
                valorContraCol = letrasPNum[contraCol]
                # chcker pra ver se repete
                espacosLivres = 0
                for i in range(valorContraCol, valorContraCol + 3):
                    if matrizMestre[x][contraLinha][i] == Fore.BLUE+"~":
                        espacosLivres += 1
                if espacosLivres == 3:
                    repetido = False

                    matrizMestre[x][contraLinha][valorContraCol:valorContraCol + 3] = Fore.LIGHTWHITE_EX+"|","=",f"|{Style.RESET_ALL}"

        #2 Submarinos  com 2 casas cada
        for i in range(2):
            repetido = True
            while repetido == True:
                print(Fore.BLUE + 25 * "-")
                subLinha =input(
                    Fore.LIGHTWHITE_EX + f"Digite um número de linha (1 a {len(matrizJUmUm[0])}) para o submarino {i+1} (2 casas): ")
                print(Fore.BLUE + 25 * "-")
                try:
                    subLinha = int(subLinha)
                except ValueError:
                    subLinha = -1
                while subLinha - 1 >= len(matrizJUmUm[1]) or subLinha - 1 < 0:
                    subLinha = input(Fore.LIGHTWHITE_EX + f"linha inválida digite um número entre 1 e {len(matrizJUmUm[0])}: ")
                    print(Fore.BLUE + 25 * "-")
                    try:
                        subLinha = int(subLinha)
                    except ValueError:
                        subLinha = -1
                subLinha -= 1
                subCol = input(Fore.LIGHTWHITE_EX + "Digite uma letra para a coluna inicial: ").lower()
                print(Fore.BLUE + 25 * "-")
                while subCol not in letrasPNum or letrasPNum[subCol] > (len(matrizJUmUm[1]) - 3):
                    subCol = input(Fore.LIGHTWHITE_EX + "letra inválida, digite denovo: ").lower()
                    print(Fore.BLUE + 25 * "-")
                valorSubCol = letrasPNum[subCol]
                # chcker pra ver se repete2
                espacosLivres = 0
                for i in range(valorSubCol, valorSubCol + 2):
                    if matrizMestre[x][subLinha][i] == Fore.BLUE+"~":
                        espacosLivres += 1
                if espacosLivres == 2:
                    repetido = False

                    matrizMestre[x][subLinha][valorSubCol:valorSubCol + 2] = Fore.LIGHTWHITE_EX+"<",f"]{Style.RESET_ALL}"


        print("\n"*100)

    # contra ia
    if int(gamemode) == 1:
        # Enc
        valorEncouracadoCol = random.randint(0, tamanho - 6)
        encouracadoLinha = random.randint(0, tamanho - 1)
        matrizMestre[2][encouracadoLinha][valorEncouracadoCol: valorEncouracadoCol + 5] = Fore.LIGHTWHITE_EX+"¬","¬","¬","¬",f"¬{Style.RESET_ALL}"

        # Port-av
        repetido = True
        while repetido:
            valorPortaAvioesCol = random.randint(0, tamanho - 5)
            portaAvioesLinha = random.randint(0, tamanho - 1)

            espacosLivres = 0
            for i in range(valorPortaAvioesCol, valorPortaAvioesCol + 4):
                if matrizMestre[2][portaAvioesLinha][i] == Fore.BLUE+"~":
                    espacosLivres += 1

            if espacosLivres == 4:
                repetido = False
                matrizMestre[2][portaAvioesLinha][valorPortaAvioesCol:valorPortaAvioesCol + 4] = Fore.LIGHTWHITE_EX+"#","#","#",f"#{Style.RESET_ALL}"

        # contra-torp
        for i in range(2):
            repetido = True
            while repetido:
                valorContraCol = random.randint(0, tamanho - 4)
                contraLinha = random.randint(0, tamanho - 1)

                espacosLivres = 0
                for i in range(valorContraCol, valorContraCol + 3):
                    if matrizMestre[2][contraLinha][i] == Fore.BLUE+"~":
                        espacosLivres += 1

                if espacosLivres == 3:
                    repetido = False
                    matrizMestre[2][contraLinha][valorContraCol:valorContraCol + 3] = Fore.LIGHTWHITE_EX+"|","=",f"|{Style.RESET_ALL}"

        # sub
        for i in range(2):
            repetido = True
            while repetido:
                valorSubCol = random.randint(0, tamanho - 3)
                subLinha = random.randint(0, tamanho - 1)

                espacosLivres = 0
                for i in range(valorSubCol, valorSubCol + 2):
                    if matrizMestre[2][subLinha][i] == Fore.BLUE+"~":
                        espacosLivres += 1

                if espacosLivres == 2:
                    repetido = False
                    matrizMestre[2][subLinha][valorSubCol:valorSubCol + 2] = Fore.LIGHTWHITE_EX+"<", f"]{Style.RESET_ALL}"

    # return
    return matrizMestre

def mostrar_tabuleiro(matrixMaster,jogador,tamanho):

    listaPrintLetra = ["---", "A", "B", "C", "D","E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                       "Q", "R", "S", "T"]

    if jogador==1:
        print(Fore.BLUE + 25 * "-")
        print(Fore.LIGHTWHITE_EX + "Tabuleiro-1")
        print(Fore.BLUE + 25 * "-")
        print(Fore.GREEN + " ".join(listaPrintLetra[0:tamanho + 1]) + Style.RESET_ALL, end="\n")
        indicadorLinha=1
        for i in range(tamanho):
            linha_colorida = f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL} " + " ".join(matrixMaster[0][i])
            if indicadorLinha < 10:
                print(linha_colorida)
            else:
                print(f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL}{' '.join(matrixMaster[0][i])}")
            indicadorLinha+=1

        print(Fore.BLUE + 25 * "-")
        print(Fore.LIGHTWHITE_EX + "Tabuleiro-2")
        print(Fore.BLUE + 25 * "-")
        print(Fore.GREEN + " ".join(listaPrintLetra[0:tamanho + 1]) + Style.RESET_ALL, end="\n")
        indicadorLinha=1
        for i in range(tamanho):
            linha_colorida = f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL} " + " ".join(matrixMaster[1][i])
            if indicadorLinha<10:
                print(linha_colorida)
            else:
                print(f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL}{' '.join(matrixMaster[1][i])}")
            indicadorLinha += 1

    elif jogador==2:
        print(Fore.BLUE + 25 * "-")
        print(Fore.LIGHTWHITE_EX + "Tabuleiro-1")
        print(Fore.BLUE + 25 * "-")
        print(Fore.GREEN + " ".join(listaPrintLetra[0:tamanho + 1]) + Style.RESET_ALL, end="\n")
        indicadorLinha = 1
        for i in range(tamanho):
            linha_colorida = f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL} " + " ".join(matrixMaster[2][i])
            if indicadorLinha<10:
                print(linha_colorida)
            else:
                print(f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL}{' '.join(matrixMaster[2][i])}")
            indicadorLinha += 1

        print(Fore.BLUE + 25 * "-")
        print(Fore.LIGHTWHITE_EX + "Tabuleiro-2")
        print(Fore.BLUE + 25 * "-")
        print(Fore.GREEN + " ".join(listaPrintLetra[0:tamanho + 1]) + Style.RESET_ALL, end="\n")
        indicadorLinha = 1
        for i in range(tamanho):
            linha_colorida = f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL} " + " ".join(matrixMaster[3][i])
            if indicadorLinha<10:
                print(linha_colorida)
            else:
                print(f"{Fore.GREEN}[{indicadorLinha}]{Style.RESET_ALL}{' '.join(matrixMaster[3][i])}")
            indicadorLinha += 1

def realizar_ataque(matrixMaster,jogador,gamemode):
    #inpt->ve se repete as jogadas-> ataca-> checa se acertou e muda na matrix
    #ainda n testei esse
    letrasPNum={
          "a": 0,
          "b": 1,
          "c": 2,
          "d": 3,
          "e": 4,
          "f": 5,
          "g": 6,
          "h": 7,
          "i": 8,
          "j": 9,
          "k": 10,
          "l": 11,
          "m": 12,
          "n": 13,
          "o": 14,
          "p": 15,
          "q": 16,
          "r": 17,
          "s": 18,
          "t": 19
    }

    if jogador==1:
        matrizSelect=1
        matrizAtacar=2
    elif jogador==2:
        matrizSelect=3
        matrizAtacar=0

    ataqueLinha=input(Fore.LIGHTWHITE_EX + "Digite um número de linha para atacar:")
    print(Fore.BLUE + 25 * "-")
    try:
        ataqueLinha = int(ataqueLinha)
    except ValueError:
        ataqueLinha = -1
    while ataqueLinha-1>len(matrixMaster[0][0]) or ataqueLinha-1<0:
        ataqueLinha = input(Fore.LIGHTWHITE_EX + "Digite uma linha válida para atacar:")
        print(Fore.BLUE + 25 * "-")
        try:
            ataqueLinha = int(ataqueLinha)
        except ValueError:
            ataqueLinha = -1
    ataqueLinha-=1
    ataqueColuna=str(input(Fore.LIGHTWHITE_EX + "Digite uma coluna para atacar"))
    print(Fore.BLUE + 25 * "-")
    while ataqueColuna not in letrasPNum:
        ataqueColuna = str(input(Fore.LIGHTWHITE_EX + "Digite uma coluna para atacar"))
        print(Fore.BLUE + 25 * "-")
    valorAtaqueColuna=letrasPNum[ataqueColuna]
    #checker pra ver se ta atacando repetido
    while matrixMaster[matrizSelect][ataqueLinha][valorAtaqueColuna]!=Fore.BLUE+"~":
        while ataqueLinha - 1 > len(matrixMaster[0][0]) or ataqueLinha - 1 < 0:
            ataqueLinha = input(Fore.LIGHTWHITE_EX + "Digite uma linha válida para atacar:")
            print(Fore.BLUE + 25 * "-")
            try:
                ataqueLinha = int(ataqueLinha)
            except ValueError:
                ataqueLinha = -1
        ataqueLinha -= 1
        ataqueColuna = str(input(Fore.LIGHTWHITE_EX + "Digite uma coluna para atacar"))
        print(Fore.BLUE + 25 * "-")
        while ataqueColuna not in letrasPNum:
            ataqueColuna = str(input(Fore.LIGHTWHITE_EX + "Digite uma coluna para atacar"))
            print(Fore.BLUE + 25 * "-")
        valorAtaqueColuna = letrasPNum[ataqueColuna]
    #checar se acertou o ataque
    if matrixMaster[matrizAtacar][ataqueLinha][valorAtaqueColuna]!=Fore.BLUE+"~":
        #avisa no tabuleiro 1 de quem é atacado e no dois
        #avisa no tab 1 de quem é atacado
        matrixMaster[matrizAtacar][ataqueLinha][valorAtaqueColuna]=Fore.RED+f"X{Style.RESET_ALL}"
        #avisa no tab 2 de quem atacou
        matrixMaster[matrizSelect][ataqueLinha][valorAtaqueColuna]=Fore.RED+f"X{Style.RESET_ALL}"
    else:
        # avisa no tab 1 de quem é atacado, é um o em maiúsculo não um zero
        matrixMaster[matrizAtacar][ataqueLinha][valorAtaqueColuna] = Fore.BLUE+ f"O"
        # avisa no tab 2 de quem atacou
        matrixMaster[matrizSelect][ataqueLinha][valorAtaqueColuna] = Fore.BLUE+f"O{Style.RESET_ALL}"

    # contra IA
    if gamemode==1:
        ataqueLinha=random.randint(1,len(matrixMaster[0][0])-1)
        ataqueColuna=random.randint(1,len(matrixMaster[0][0])-1)

        #checker p ver se repete
        while matrixMaster[3][ataqueLinha][ataqueColuna]!=Fore.BLUE+"~":
            ataqueLinha = random.randint(1, len(matrixMaster[0][0]) - 1)
            ataqueColuna = random.randint(1, len(matrixMaster[0][0]) - 1)

        #avisa player q a "IA" acertou
        if matrixMaster[0][ataqueLinha][ataqueColuna] != Fore.BLUE+"~":
            matrixMaster[0][ataqueLinha][ataqueColuna] = Fore.RED+f"X{Style.RESET_ALL}"
            matrixMaster[3][ataqueLinha][ataqueColuna] = Fore.RED+f"X{Style.RESET_ALL}"

        # avisa player q a "IA" acertou
        else:
            matrixMaster[0][ataqueLinha][ataqueColuna] = Fore.BLUE+f"O{Style.RESET_ALL}"
            matrixMaster[3][ataqueLinha][ataqueColuna] = Fore.BLUE+f"O{Style.RESET_ALL}"

    return matrixMaster

def verificar_vitoria(matrixMaster,tamanho,nameP1,nameP2):
    #checker
    vitoria = False
    vencedor=[]
    counter=0
    for i in range(tamanho):
        for j in range(tamanho):
            if matrixMaster[2][i][j] == Fore.RED+f"X{Style.RESET_ALL}":
                counter += 1
    #numero maximo de posiçoes derrubadas é 19
    if counter == 19:
        vitoria = True
        vencedor=[f"{nameP1} venceu"]
    #vou fzr um pro jogador 1 e dois ou bot
    counter=0
    for i in range(tamanho):
        for j in range(tamanho):
            if matrixMaster[0][i][j]==Fore.RED+f"X{Style.RESET_ALL}":
                counter+=1
    if counter == 19:
        vitoria = True
        vencedor=[f"{nameP2} venceu"]
    resposta = input("Digite s para encerrar: ")
    return resposta.lower() == 's',vitoria,vencedor

def delay():
    print("\n"*100)
    time.sleep(2)


#esqueleto do jogo em si
sairDoJogo=False
while not sairDoJogo:
    modoJogo,nomeJUm,nomeJdois=menu_inicial()
    tamanho=configurar_tabuleiro()
    matrizMestre = posicionar_navios(modoJogo,tamanho)
    #aqui faz um loop
    encerrar = False
    vitoria = False
    #aqui vai rodar enq for falso
    while not vitoria and not encerrar:
        if modoJogo == "1":
            # Contra PC
            mostrar_tabuleiro(matrizMestre, 1, tamanho)
            matrizMestre = realizar_ataque(matrizMestre, 1,1)
            encerrar, vitoria,vencedor = verificar_vitoria(matrizMestre, tamanho,nomeJUm,nomeJdois)
            delay()
        else:
            # PVP
            for jogador in [1, 2]:
                #enq for falso vai sempre cair nisso
                if not vitoria and not encerrar:
                    mostrar_tabuleiro(matrizMestre, jogador, tamanho)
                    matrizMestre = realizar_ataque(matrizMestre, jogador,2)
                    encerrar, vitoria,vencedor = verificar_vitoria(matrizMestre, tamanho,nomeJUm,nomeJdois)
                    delay()

    #add histórico no txt, eu vi um video no yt pra aprender isso
    # dps dei uma pesquisada e recomendou o encoding pra acento e tal
    historico=open("historico.txt", "a", encoding="utf-8")
    historico.write(f"{vencedor}\n")
    historico.close()

    print(f"o vencedor é {vencedor}, e o histórico está disponível no historico.txt para consulta")
    respostaSairDoJogo=input(f"se você deseja sair do jogo digite s:")
    if respostaSairDoJogo=="s":
        sairDoJogo=True