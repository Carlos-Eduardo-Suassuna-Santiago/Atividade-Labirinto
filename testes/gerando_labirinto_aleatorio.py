import random
import os 

os.system('cls')
def gera_labirinto(linhas, colunas):
    labirinto = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if i == 0 or i == linhas - 1 or j == 0 or j == colunas - 1:
                linha.append("#")
            else:
                linha.append(" ")
        labirinto.append(linha)

    start = (random.randint(1, linhas - 2), 0)
    exit = (random.randint(1, linhas - 2), colunas - 1)
    labirinto[start[0]][start[1]] = "E"
    labirinto[exit[0]][exit[1]] = "S"

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            if random.random() > 0.5:
                labirinto[i][j] = "#"
    return labirinto

def imprime_labirinto(labirinto_map):
    for linha in labirinto_map:
        print(" ".join(linha))

labirinto = gera_labirinto(30, 30)
imprime_labirinto(labirinto)
