"""Este programa Python é usado para resolver um labirinto e encontrar o caminho do início ao fim. 
O programa começa limpando a tela. Em seguida, uma classe labirinto é criada com os seguintes métodos:"""

import os
import sys
import pygame
import keyboard as kb
from time import sleep
from colorama import Fore, Style

os.system('cls')
pygame.init()
opcao = "s"

while opcao == "s":
    class Labirinto:
        def __init__(self, labirinto_map):
            """Este método inicializa o labirinto, definindo as variáveis 
            labirinto_map, start, exit, linha, coluna, visitou, pilha e caminho."""
            self.labirinto_map = labirinto_map
            self.start = None
            self.exit = None
            self.linha = len(labirinto_map)
            self.coluna = len(labirinto_map[0])
            self.visitou = [[False for j in range(self.coluna)] for i in range(self.linha)]
            self.pilha = []
            self.caminho = {}

        def achar_inicio_fim(self):
            """Este método encontra as coordenadas dos pontos inicial e final do labirinto."""
            for i in range(self.linha):
                for j in range(self.coluna):
                    if self.labirinto_map[i][j] == '\U0001F7E2':
                        self.start = (i, j)
                    elif self.labirinto_map[i][j] == '\U0001F9C0':
                        self.exit = (i, j)

        def validacao(self, x, y):
            """Este método verifica se as coordenadas fornecidas são válidas e se a célula naquele 
            local não é uma parede ou já foi visitada."""
            if x < 0 or x >= self.linha or y < 0 or y >= self.coluna:
                return False
            if self.labirinto_map[x][y] == '\U0001F9F1' or self.visitou[x][y]:
                return False
            return True

        def achar_saida(self):
            """Este método encontra a saída do labirinto usando um algoritmo Depth First Search (DFS). 
            O algoritmo começa no ponto inicial e, em seguida, verifica cada um de seus vizinhos para 
            ver se é válido. Se for válido, o algoritmo continua até aquele ponto e verifica seus vizinhos. 
            Isso continua até que o ponto final seja alcançado ou o algoritmo não consiga mais encontrar vizinhos válidos.
            """
            self.achar_inicio_fim()
            self.pilha.append(self.start)
            self.visitou[self.start[0]][self.start[1]] = True
            self.caminho[self.start] = None

            while len(self.pilha) > 0:
                atual = self.pilha.pop()
                if atual == self.exit:
                    print(Fore.GREEN +"Saida encontrada\n"+ Style.RESET_ALL)
                    pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
                    pygame.mixer.music.load('musicas/efeitos/win.mp3')
                    pygame.mixer.music.play(0)
                    sleep(6)
                    self.atualizar_labirinto(atual)
                    self.print_caminho()
                    return
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x = atual[0] + dx
                    y = atual[1] + dy
                    if self.validacao(x, y):
                        self.pilha.append((x, y))
                        self.visitou[x][y] = True
                        self.caminho[(x, y)] = atual
                        self.atualizar_labirinto((x, y))
    
            print(Fore.RED +"Saida não encontrada\n"+ Style.RESET_ALL)
            pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
            pygame.mixer.music.load('musicas/efeitos/lose.mp3')
            pygame.mixer.music.play(0)
            sleep(4)
            os.system("cls")

        def print_caminho(self):
            """Este método imprime as coordenadas do caminho percorrido do ponto inicial ao ponto final. 
            Ele também anexa as coordenadas a um arquivo chamado "caminho.txt"."""

            arquivo = open("caminho.txt", "a")
            arquivo.write("COORDENADAS\n")
            atual = self.exit
            while atual:
                x, y = atual
                #print(f"({x}, {y})^\n", end="")
                atual = self.caminho[atual]
                arquivo = open("caminho.txt", "a")
                arquivo.write(f"\n({x}, {y})^")

        def atualizar_labirinto(self, atual):
            """Este método atualiza o mapa do labirinto alterando a célula nas coordenadas fornecidas para 'M'. 
            Em seguida, imprime o mapa do labirinto, com um atraso de 1 segundo."""
            
            print(Fore.GREEN +"\nLabirinto em execução\n"+ Style.RESET_ALL)

            x, y = atual
            self.labirinto_map[x][y] = "\U0001F400"
            
            for i in self.labirinto_map:
                print(" ".join(i))
            sleep(0.3)
            os.system('cls')
            
    print(Fore.RED +"""
            **********************************
            *                                *
            * BEM VINDO AO LABIRINTO DO RATO *
            *                                *
            **********************************
        """+ Style.RESET_ALL)
    pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
    pygame.mixer.music.load('musicas/menu/menu.mp3')
    pygame.mixer.music.play(-1)
    print(Fore.YELLOW +"""
    \nMENU:\n
    [S] = start\n
    [I] = informações\n
    [E] = exit\n         
        """+ Style.RESET_ALL)
    start = False
    finish = False
    mapa = False
    animacao = False

    while start == False:
        if kb.is_pressed('s'):
            start = True
            print(Fore.YELLOW +"De qual Labirinto você deseja? [1] / [2]: "+ Style.RESET_ALL)
            print("\n")

            while mapa == False:
                if kb.is_pressed('1'):
                    mapa = True
                    pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
                    pygame.mixer.music.load('musicas/map.mp3')
                    pygame.mixer.music.play()
                    labirinto_map_matriz = [
                ["1", "1", "1", "S", "1", "1", "1", "1", "1", "1", "1", "1"],
                ["1", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0", "1"],
                ["1", "0", "1", "0", "1", "1", "0", "1", "1", "1", "0", "1"],
                ["1", "0", "1", "0", "0", "1", "0", "0", "1", "1", "0", "1"],
                ["1", "0", "1", "1", "0", "1", "1", "0", "1", "1", "0", "1"],
                ["1", "0", "0", "1", "0", "0", "0", "0", "1", "1", "0", "1"],
                ["1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
                ["1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
                ["1", "1", "0", "0", "1", "1", "1", "1", "0", "0", "0", "1"],
                ["1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1"],
                ["1", "1", "1", "0", "0", "1", "1", "1", "0", "1", "1", "1"],
                ["1", "0", "1", "0", "0", "1", "1", "1", "0", "1", "1", "1"],
                ["1", "0", "0", "0", "1", "1", "1", "1", "0", "1", "1", "1"],
                ["1", "1", "1", "0", "1", "1", "1", "1", "0", "0", "0", "1"],
                ["1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
                ["1", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
                ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
                ["1", "0", "1", "0", "0", "0", "0", "0", "0", "0", "1", "1"],
                ["1", "0", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1"],
                ["1", "0", "0", "1", "0", "1", "1", "1", "1", "0", "1", "1"],
                ["1", "1", "0", "1", "1", "1", "0", "0", "0", "0", "1", "1"],
                ["1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1"],
                ["1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1"],
                ["1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1", "1"],
                ["1", "0", "1", "0", "0", "1", "0", "0", "0", "1", "1", "1"],
                ["1", "0", "1", "1", "0", "1", "1", "1", "0", "1", "0", "E"],
                ["1", "0", "0", "0", "1", "1", "1", "1", "0", "0", "0", "1"],
                ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
            ]
                    
                    labirinto_map_caminho = [
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F7E2", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "  ", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "\U0001F9F1", "  ", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9C0"],
                ["\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"]
            ]
                    labirinto_map = labirinto_map_matriz and labirinto_map_caminho

                    labirinto = Labirinto(labirinto_map)
                    labirinto.achar_saida()
                elif kb.is_pressed('2'):
                    mapa = True
                    pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
                    pygame.mixer.music.load('musicas/map.mp3')
                    pygame.mixer.music.play()
                    labirinto_map_matriz = [
                ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                ["S", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "1"],
                ["1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "0", "1"],
                ["1", "0", "0", "0", "1", "1", "1", "0", "1", "1", "0", "1"],
                ["1", "0", "1", "1", "1", "1", "0", "0", "0", "1", "0", "1"],
                ["1", "0", "1", "1", "1", "1", "0", "1", "0", "1", "0", "1"],
                ["1", "0", "0", "0", "1", "1", "0", "1", "0", "1", "0", "1"],
                ["1", "0", "1", "0", "1", "1", "0", "1", "0", "1", "0", "1"],
                ["1", "0", "1", "0", "0", "1", "0", "1", "0", "1", "0", "1"],
                ["1", "0", "1", "1", "0", "1", "1", "1", "0", "1", "0", "1"],
                ["1", "0", "1", "1", "0", "0", "0", "1", "0", "1", "0", "1"],
                ["1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "0", "1"],
                ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "0", "1"],
                ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
                ["1", "0", "0", "0", "0", "0", "0", "0", "1", "1", "0", "1"],
                ["1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "0", "1"],
                ["1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "0", "1"],
                ["1", "0", "0", "0", "1", "0", "1", "1", "1", "1", "0", "1"],
                ["1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "0", "1"],
                ["1", "1", "1", "0", "1", "0", "1", "1", "0", "1", "1", "1"],
                ["1", "1", "0", "0", "1", "0", "1", "1", "0", "1", "1", "1"],
                ["1", "1", "0", "0", "1", "0", "1", "1", "0", "1", "1", "1"],
                ["1", "0", "0", "1", "1", "0", "1", "1", "0", "1", "1", "1"],
                ["1", "0", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1"],
                ["1", "0", "1", "1", "1", "0", "1", "0", "0", "1", "1", "1"],
                ["1", "1", "1", "0", "0", "0", "1", "0", "1", "1", "1", "E"],
                ["1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "1"],
                ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
            ]
                    labirinto_map_caminho = [
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F7E2", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1", "  ", "  ", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "\U0001F9F1", "  ", "\U0001F9F1", "\U0001F9F1", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "  ", "  ", "  ", "  ", "\U0001F9F1"],
                ["\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9C0", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1", "\U0001F9F1"]
            ]
                    labirinto_map = labirinto_map_matriz and labirinto_map_caminho
                    labirinto = Labirinto(labirinto_map)
                    labirinto.achar_saida()
        elif kb.is_pressed('i'):
            start = True
            pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
            pygame.mixer.music.load('musicas/informacoes/informacoes.mp3')
            pygame.mixer.music.play(-1)
            os.system("cls")
            print(Fore.YELLOW +"""
                ***************************************************************************
                *                                                                         *
                *                              INFORMAÇÕES                                *
                *                                                                         *
                *  Atividade desenvolvida para matéria de Estrutura de Dados Lineares.    *
                *  A atividade consiste em um ratinho descobrir a saida de uma labirinto, *
                *  a solução deve ser feita usando a estrutura de dados PILHA para nosso  *
                *  querido ratinho encontrar a sainda do seu tormento chamado labirinto.  *
                *                                                                         *
                ***************************************************************************

                                                (\__/)
                                               (='.'=) 
                                               (\___/)   ...
                                               (")_(")../
                """+ Style.RESET_ALL)
            while finish == False:
                if kb.is_pressed('q'):
                    finish = True
                    os.system("cls")
        elif kb.is_pressed('e'):
            pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
            pygame.mixer.music.load('musicas/exit.mp3')
            pygame.mixer.music.play()
            start = True
            while 1:
                os.system("cls")
                print(Fore.YELLOW +"Obrigado por utilizar nosso software\n"+ Style.RESET_ALL)
                print("""
                                  (\__/)
                                 (='.'=) 
                                 (\___/)   ...
                                 (")_(")../
                """)
                sleep(0.1)
                os.system('cls')
                print(Fore.YELLOW +"Obrigado por utilizar nosso software\n"+ Style.RESET_ALL)
                print("""
                                     (\__/)
                                     (='.'=) 
                               ...   (\___/)
                                  \..(")_(")
                """)
                sleep(0.1)
                os.system('cls')
                if kb.is_pressed('q'):
                    finish = False
                    os.system("cls")
                    sys.exit()
            while finish == False:
                if kb.is_pressed('q'):
                    finish = True
                    os.system("cls")
                    sys.exit()
