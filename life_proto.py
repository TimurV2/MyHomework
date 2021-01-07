import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:

    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10 ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.draw_grid()
            self.draw_lines()
            self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        grid = [[None for _ in range(self.cell_width)] for _ in range(self.cell_height)]
        if randomize != 0:
            for i in range(self.cell_height):
                for j in range(self.cell_width):
                    grid[i][j] = random.randint(0, 1)
        else:
            for i in range(self.cell_height):
                for j in range(self.cell_width):
                    grid[i][j] = 0
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 255, 0), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))


    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        x, y = cell
        cells = []
        if ((x >= 1) and (x < game.cell_height-1)) and ((y >= 1) and (y < game.cell_width-1)):
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                        cells.append(self.grid[i][j])
            cells.pop(4)
        else:
            if x == 0:
                if y == 0:
                    cells.append(self.grid[x][y+1])
                    cells.append(self.grid[x+1][y])
                    cells.append(self.grid[x+1][y+1])
                if y == game.cell_width - 1:
                    cells.append(self.grid[x][y-1])
                    cells.append(self.grid[x+1][y-1])
                    cells.append(self.grid[x+1][y])
            elif x == game.cell_height - 1:
                if y == 0:
                    cells.append(self.grid[x-1][y])
                    cells.append(self.grid[x-1][y+1])
                    cells.append(self.grid[x][y+1])
                if y == game.cell_width - 1:
                    cells.append(self.grid[x-1][y-1])
                    cells.append(self.grid[x-1][y])
                    cells.append(self.grid[x][y-1])
        if ((x == 0) or (x == game.cell_height-1)) and ((y >= 1) and (y < game.cell_width-1)):
            if x == 0:
                for i in range(x, x+2):
                    for j in range(y-1, y+2):
                        cells.append(self.grid[i][j])
                cells.pop(1)
            else:
                for i in range(x-1, x+1):
                    for j in range(y-1, y+2):
                        cells.append(self.grid[i][j])
                cells.pop(4)
        if ((y == 0) or (y == game.cell_width-1)) and ((x >= 1) and (x < game.cell_height-1)):
            if y == 0:
                for i in range(x-1, x+2):
                    for j in range(y, y+2):
                        cells.append(self.grid[i][j])
                cells.pop(2)
            else:
                for i in range(x-1, x+2):
                    for j in range(y-1, y+1):
                        cells.append(self.grid[i][j])
                cells.pop(3)
        return cells

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        dead = []
        alive = []
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if (sum(self.get_neighbours((i, j))) == 3) and (self.grid[i][j] == 0):
                    alive.append((i, j))
                elif (sum(self.get_neighbours((i, j))) < 2) or (sum(self.get_neighbours((i, j))) > 3):
                    dead.append((i, j))
        for i in alive:
            self.grid[i[0]][i[1]] = 1
        for i in dead:
            self.grid[i[0]][i[1]] = 0
        return self.grid

if __name__ == '__main__':
    game = GameOfLife(900, 900, 9)
    game.run()
