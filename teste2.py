import random

# Função para gerar o labirinto aleatório
def gerar_labirinto(linhas, colunas):
    labirinto = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append("#" if random.random() < 0.3 else " ")
        labirinto.append(linha)
    return labirinto

# Função para encontrar o caminho de saída usando pilhas
def encontrar_saida(labirinto):
    linhas = len(labirinto)
    colunas = len(labirinto[0])
    pilha = []
    posicao_inicial = None
    for i in range(linhas):
        for j in range(colunas):
            if labirinto[i][j] == " ":
                posicao_inicial = (i, j)
                break
        if posicao_inicial:
            break
    if not posicao_inicial:
        return None
    pilha.append(posicao_inicial)
    while pilha:
        i, j = pilha[-1]
        labirinto[i][j] = "X"
        if (i == 0 or labirinto[i-1][j] == "#") and (i == linhas-1 or labirinto[i+1][j] == "#") and (j == 0 or labirinto[i][j-1] == "#") and (j == colunas-1 or labirinto[i][j+1] == "#"):
            return pilha
        if i > 0 and labirinto[i-1][j] == " ":
            pilha.append((i-1, j))
        elif i < linhas-1 and labirinto[i+1][j] == " ":
            pilha.append((i+1, j))
        elif j > 0 and labirinto[i][j-1] == " ":
            pilha.append((i, j-1))
        elif j < colunas-1 and labirinto[i][j+1] == " ":
            pilha.append((i, j+1))
        else:
            pilha.pop()
    return None

# Testando o código
labirinto = gerar_labirinto(10, 10)
for linha in labirinto:
    print("".join(linha))
print("Caminho de saída:", encontrar_saida(labirinto))
for linha in labirinto:
    print("".join(linha))
