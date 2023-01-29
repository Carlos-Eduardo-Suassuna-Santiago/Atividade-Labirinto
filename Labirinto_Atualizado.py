
"""Este programa Python é usado para resolver um labirinto e encontrar o caminho do início ao fim. 
O programa começa limpando a tela. Em seguida, uma classe labirinto é criada com os seguintes métodos:"""

import os
from time import sleep

os.system('cls')
sleep(3)
class Labirinto:
    def __init__(self, labirinto_map):
        """Este método inicializa o labirinto, definindo as variáveis 
        ​​labirinto_map, start, end, linha, coluna, visitou, pilha e caminho."""
        self.labirinto_map = labirinto_map
        self.start = None
        self.end = None
        self.linha = len(labirinto_map)
        self.coluna = len(labirinto_map[0])
        self.visitou = [[False for j in range(self.coluna)] for i in range(self.linha)]
        self.pilha = []
        self.caminho = {}

    def find_start_end(self):
        """Este método encontra as coordenadas dos pontos inicial e final do labirinto."""
        for i in range(self.linha):
            for j in range(self.coluna):
                if self.labirinto_map[i][j] == 'S':
                    self.start = (i, j)
                elif self.labirinto_map[i][j] == 'E':
                    self.end = (i, j)

    def is_valid(self, x, y):
        """Este método verifica se as coordenadas fornecidas são válidas e se a célula naquele 
        local não é uma parede ou já foi visitada."""
        if x < 0 or x >= self.linha or y < 0 or y >= self.coluna:
            return False
        if self.labirinto_map[x][y] == '#' or self.visitou[x][y]:
            return False
        return True

    def find_exit(self):
        """Este método encontra a saída do labirinto usando um algoritmo Depth First Search (DFS). 
        O algoritmo começa no ponto inicial e, em seguida, verifica cada um de seus vizinhos para 
        ver se é válido. Se for válido, o algoritmo continua até aquele ponto e verifica seus vizinhos. 
        Isso continua até que o ponto final seja alcançado ou o algoritmo não consiga mais encontrar vizinhos válidos.
        """
        self.find_start_end()
        self.pilha.append(self.start)
        self.visitou[self.start[0]][self.start[1]] = True
        self.caminho[self.start] = None

        while len(self.pilha) > 0:
            current = self.pilha.pop()
            if current == self.end:
                print("Found the exit!")
                self.update_labirinto(current)
                self.print_caminho()
                return
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = current[0] + dx
                y = current[1] + dy
                if self.is_valid(x, y):
                    self.pilha.append((x, y))
                    self.visitou[x][y] = True
                    self.caminho[(x, y)] = current
                    self.update_labirinto((x, y))

        print("Exit not found!")

    def print_caminho(self):
        """Este método imprime as coordenadas do caminho percorrido do ponto inicial ao ponto final. 
        Ele também anexa as coordenadas a um arquivo chamado "caminho.txt"."""
        arquivo = open("caminho.txt", "a")
        arquivo.write("COORDENADAS\n")
        current = self.end
        while current:
            x, y = current
            print(f"({x}, {y})^\n", end="")
            current = self.caminho[current]
            arquivo = open("caminho.txt", "a")
            arquivo.write(f"\n({x}, {y})^")

    def update_labirinto(self, current):
        """Este método atualiza o mapa do labirinto alterando a célula nas coordenadas fornecidas para 'M'. 
        Em seguida, imprime o mapa do labirinto, com um atraso de 1 segundo."""
        x, y = current
        self.labirinto_map[x][y] = 'M'
        for i in self.labirinto_map:
            print(i)
        sleep(1)
        os.system('cls')

labirinto_map = [
    ["S", "#", "#", "#", "#", "#"],
    [" ", " ", " ", " ", "#", "#"],
    [" ", " ", "#", " ", "#", "#"],
    ["#", " ", "#", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", "#", " ", "#"],
    ["#", "#", " ", "#", "#", "#"],
    ["#", "#", " ", "#", "#", "#"],
    ["#", "#", " ", " ", "#", "#"],
    ["#", "#", "#", " ", "#", "#"],
    ["#", " ", "#", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", " ", "E"]
]

labirinto = Labirinto(labirinto_map)
labirinto.find_exit()
