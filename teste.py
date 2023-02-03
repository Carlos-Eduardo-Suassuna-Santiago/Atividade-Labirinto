import pygame

# Inicialização do Pygame
pygame.init()

# Definindo tamanho da tela
screen = pygame.display.set_mode((600, 400))

# Define a cor de fundo da tela
background_color = (255, 255, 255)

# Define a cor das paredes
wall_color = (0, 0, 0)

# Define a cor do caminho
path_color = (255, 255, 255)

# Carrega a matriz que representa o labirinto
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Desenha o labirinto na tela
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 1:
            pygame.draw.rect(screen, wall_color, (j*60, i*60, 60, 60))
        else:
            pygame.draw.rect(screen, path_color, (j*60, i*60, 60, 60))

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
