import os
from time import sleep

os.system('cls')
sleep(3)
class Maze:
    def __init__(self, maze_map):
        self.maze_map = maze_map
        self.start = None
        self.end = None
        self.row = len(maze_map)
        self.col = len(maze_map[0])
        self.visited = [[False for j in range(self.col)] for i in range(self.row)]
        self.stack = []
        self.path = {}

    def find_start_end(self):
        for i in range(self.row):
            for j in range(self.col):
                if self.maze_map[i][j] == 'S':
                    self.start = (i, j)
                elif self.maze_map[i][j] == 'E':
                    self.end = (i, j)

    def is_valid(self, x, y):
        if x < 0 or x >= self.row or y < 0 or y >= self.col:
            return False
        if self.maze_map[x][y] == '#' or self.visited[x][y]:
            return False
        return True

    def find_exit(self):
        self.find_start_end()
        self.stack.append(self.start)
        self.visited[self.start[0]][self.start[1]] = True
        self.path[self.start] = None

        while len(self.stack) > 0:
            current = self.stack.pop()
            if current == self.end:
                print("Found the exit!")
                self.update_maze(current)
                self.print_path()
                return
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = current[0] + dx
                y = current[1] + dy
                if self.is_valid(x, y):
                    self.stack.append((x, y))
                    self.visited[x][y] = True
                    self.path[(x, y)] = current
                    self.update_maze((x, y))

        print("Exit not found!")

    def print_path(self):
        arquivo = open("caminho.txt", "a")
        arquivo.write("COORDENADAS\n")
        current = self.end
        while current:
            x, y = current
            print(f"({x}, {y})^\n", end="")
            current = self.path[current]
            arquivo = open("caminho.txt", "a")
            arquivo.write(f"\n({x}, {y})^")

    def update_maze(self, current):
        x, y = current
        self.maze_map[x][y] = 'M'
        for i in self.maze_map:
            print(i)
        sleep(1)
        os.system('cls')

maze_map = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', '#', '#'],
    [' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', ' ', 'E']
]

maze = Maze(maze_map)
maze.find_exit()
