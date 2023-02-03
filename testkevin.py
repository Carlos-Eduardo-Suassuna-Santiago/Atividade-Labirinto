import os
from time import sleep

# Define o labirinto como uma matriz
maze = [    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Define a posição inicial e a posição final
start = (1, 1)
end = (1, 6)

# Define a direção para cada movimento
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Define a pilha para armazenar o caminho
stack = [start]

# Define a matriz para marcar os lugares visitados
visited = [[False for j in range(len(maze[0]))] for i in range(len(maze))]
visited[start[0]][start[1]] = True

# Define a variável para armazenar o caminho
path = []

# Enquanto a pilha não estiver vazia
while stack:
    # Pega a última posição na pilha
    curr_pos = stack.pop()

    # Adiciona a posição atual ao caminho
    path.append(curr_pos)

    # Se a posição atual é o final, interrompe o loop
    if curr_pos == end:
        break

    # Verifica os próximos movimentos possíveis
    for i in range(4):
        new_x = curr_pos[0] + dx[i]
        new_y = curr_pos[1] + dy[i]
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and not visited[new_x][new_y] and maze[new_x][new_y] == 0:
            stack.append((new_x, new_y))
            visited[new_x][new_y] = True

    # Atualiza o labirinto com o caminho percorrido até o momento
    for i in range(len(path)):
        x, y = path[i]
        maze[x][y] = 2

    # Imprime o labirinto atualizado com o caminho
    for row in maze:
        print(row)
        
    sleep(0.5)
    os.system("cls")

# Verifica se o caminho foi encontrado ou não
if path[-1] == end:
    print("Caminho encontrado: ", path)
else:
    print("Caminho não encontrado.")