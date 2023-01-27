class Labirinto:

    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.start = None
        self.end = None
        self.pilha = []
        self.visitou = set()
        self.caminho = {}

        for i in range(len(labirinto)):
            for j in range(len(labirinto[i])):
                if labirinto[i][j] == "S":
                    self.start = (i, j)
                elif labirinto[i][j] == "E":
                    self.end = (i, j)

    def pilha_resolver(self):
        self.pilha.append(self.start)
        while self.pilha:
            atual = self.pilha.pop()
            if atual == self.end:
                print("Achei a saida\n")
                self.print_caminho(atual)
                return True
            self.visitou.add(atual)
            for vizinho in self.get_vizinhos(atual):
                if vizinho not in self.visitou:
                    self.caminho[vizinho] = atual
                    self.pilha.append(vizinho)
        print("Não achei a saida")
        return False

    def get_vizinhos(self, posicao):
        vizinhos = []
        x, y = posicao
        if x > 0 and self.labirinto[x-1][y] != "#":
            vizinhos.append((x-1, y))
        if x < len(self.labirinto)-1 and self.labirinto[x+1][y] != "#":
            vizinhos.append((x+1, y))
        if y > 0 and self.labirinto[x][y-1] != "#":
            vizinhos.append((x, y-1))
        if y < len(self.labirinto[0])-1 and self.labirinto[x][y+1] != "#":
            vizinhos.append((x, y+1))
        return vizinhos

    def print_caminho(self, posicao):
        caminho = [posicao]
        while posicao != self.start:
            posicao = self.caminho[posicao]
            caminho.append(posicao)
        for posicao in reversed(caminho):
            x, y = posicao
            arquivo = open("caminho.txt", "a")
            arquivo.write(f"({x} , {y})\n")
            #print(f"({x}, {y})")
        print("As coordenadas com o passo a passo do caminho percorrido se encontra no arquivo dentro da referente pasta da atividade")

# Example usage
labirinto = [
    ["S", "#", "#", "#", "#", "#"],
    [".", "#", ".", ".", "#", "#"],
    [".", ".", "#", ".", "#", "#"],
    ["#", ".", "#", ".", ".", "#"],
    ["#", ".", "#", "#", ".", "#"],
    ["#", ".", ".", ".", ".", "#"],
    ["#", "#", ".", "#", "#", "#"],
    ["#", "#", ".", "#", "#", "#"],
    ["#", "#", ".", ".", "#", "#"],
    ["#", "#", "#", ".", "#", "#"],
    ["#", ".", "#", ".", ".", "#"],
    ["#", ".", "#", "#", ".", "#"],
    ["#", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", ".", "E"]
]

labirinto = Labirinto(labirinto)
labirinto.pilha_resolver()

print("\nLabirinto Finalizado\n")