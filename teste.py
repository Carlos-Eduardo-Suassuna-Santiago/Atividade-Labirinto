import pygame

# Inicialização do Pygame
pygame.init()

# Definindo tamanho da tela
screen = pygame.display.set_mode((240, 560))

# Define a cor das paredes
wall_color = (0, 0, 255)

# Define a cor do caminho
path_color = (255, 255, 255)

# Carrega a matriz que representa o labirinto
labirinto_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Desenha o labirinto na tela
for i in range(len(labirinto_map)):
    for j in range(len(labirinto_map[i])):
        if labirinto_map[i][j] == 1:
            pygame.draw.rect(screen, wall_color, (j*20, i*20, 20, 20))
        else:
            pygame.draw.rect(screen, path_color, (j*20, i*20, 20, 20))

# Atualiza a tela
pygame.display.update()

# Executa o loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Finaliza o Pygame
pygame.quit()
