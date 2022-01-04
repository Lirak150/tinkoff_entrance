from Field import Field
import pygame
import time
from pygame.locals import QUIT

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCALE = 20


class Game:
    def __init__(self, n=40, m=40):
        self._field = Field(n, m)
        self._n = n
        self._m = m
        self.root = pygame.display.set_mode((n * SCALE, m * SCALE))

    def print_field(self):
        self.root.fill(WHITE)

        for i in range(0, self.root.get_height() // SCALE):
            pygame.draw.line(self.root, BLACK, (0, i * SCALE),
                             (self.root.get_width(), i * SCALE))
        for j in range(0, self.root.get_width() // SCALE):
            pygame.draw.line(self.root, BLACK, (j * SCALE, 0),
                             (j * SCALE, self.root.get_height()))
        for i in pygame.event.get():
            if i.type == QUIT:
                quit()
        for i in range(self._n):
            for j in range(self._m):
                pygame.draw.rect(self.root,
                                 (255 * self._field.field[i][
                                     j].num_repr() % 256, 0, 0),
                                 [i * SCALE, j * SCALE, SCALE, SCALE])
            # Обновляем экран
        pygame.display.update()

    def start_game(self):
        while self._field.update_field():
            self.print_field()
            time.sleep(0.25)
