import random
from Cell import Cell
from copy import deepcopy


class Field:
    def __init__(self, n, m):
        self._field = [[Cell(bool(random.getrandbits(1))) for _ in range(m)]
                       for _ in range(n)]
        self._n = n
        self._m = m

    def count_alive_around_cell(self, x, y):
        delta_x = [-1, 0, 1]
        delta_y = [-1, 0, 1]
        count = 0
        for x_del in delta_x:
            for y_del in delta_y:
                if delta_x == delta_y and delta_x == 0:
                    continue
                if (self._field[(x + x_del + self._n) % self._n][
                    (y + y_del + self._n) % self._n].is_alive):
                    count += 1
        return count

    def count_all_alive(self):
        count = 0
        for row in self._field:
            for cell in row:
                count += 1 if cell.is_alive else 0
        return count

    def get_next_generation(self):
        new_field = deepcopy(self._field)
        for i in range(self._n):
            for j in range(self._m):
                count_alive_cells = self.count_alive_around_cell(i, j)
                if not self._field[i][j].is_alive:
                    if count_alive_cells == 3:
                        new_field[i][j].make_alive()
                else:
                    if count_alive_cells < 2 or count_alive_cells > 3:
                        new_field[i][j].make_dead()
        return new_field

    def update_field(self):
        new_field = self.get_next_generation()
        if self._field == new_field:
            return 0
        self._field = new_field
        if self.count_all_alive() == 0:
            return 0
        return 1

    @property
    def field(self):
        return self._field
