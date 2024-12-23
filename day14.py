from dataclasses import dataclass
from math import prod
import re

@dataclass
class Worker:
    start: tuple
    dx: int
    dy: int

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.workers = []
    
    def add_worker(self, start, dx, dy):
        self.workers.append(Worker(start, dx, dy))

    def get_positions(self, steps):
        positions = []
        for w in self.workers:
            pos = ((w.start[0] + w.dx * steps) % self.height,
                   (w.start[1] + w.dy * steps) % self.width)
            positions.append(pos)
        return positions
    
    def get_grid(self, steps):
        positions = self.get_positions(steps)
        grid = [[0] * self.width for _ in range(self.height)]
        for p in positions:
            grid[p[0]][p[1]] += 1
        return grid

    def get_safety_factor(self, steps):
        grid = self.get_grid(steps)
        scores = [0, 0, 0, 0]
        mid_r = self.height // 2
        mid_c = self.width // 2
        for r, row in enumerate(grid):
            if r < mid_r:
                scores[0] += sum(row[:mid_c])
                scores[1] += sum(row[mid_c + 1:])
            elif r > mid_r:
                scores[2] += sum(row[:mid_c])
                scores[3] += sum(row[mid_c + 1:])
        return prod(scores, start=1)

    def display(self, steps, numeric=True):
        grid = self.get_grid(steps)
        for row in grid:
            for x in row:
                if x == 0:
                    print(".", end="")
                else:
                    print(x if numeric else "#", end="")
            print()

def parse_input():
    grid = Grid(103, 101)
    with open("input/day14.txt", "r") as f:
        for line in f:
            m = re.search(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line.rstrip())
            # Note inversion of x-y convention here (x = rows, y = cols)
            sy, sx, dy, dx = [int(x) for x in m.groups()]
            grid.add_worker((sx, sy), dx, dy)
    
    return grid

def part_one():
    grid = parse_input()
    grid.display(100)
    print(grid.get_safety_factor(100))

def part_two():
    grid = parse_input()
    
    # Pattern will repeat every (101 x 103) iterations
    safety_factors = [grid.get_safety_factor(i) for i in range(101 * 103)]
    print(max(safety_factors))
    print(min(safety_factors))

    # Educated guess that the Christmas tree occurs at the min safety factor
    # since most of the workers will be clustered in one quadrant
    i = safety_factors.index(min(safety_factors))
    # Check!
    grid.display(i)
    print(i)

if __name__ == "__main__":
    part_one()
    part_two()