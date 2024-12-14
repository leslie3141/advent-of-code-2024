from collections import defaultdict
import copy
import itertools

def get_antenna_locations(grid):
    antennae = defaultdict(list)
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c != ".":
                antennae[c].append((i, j))
    
    return antennae

def print_grid(grid, antinodes):
    full_grid = copy.deepcopy(grid)
    for node in antinodes:
        if full_grid[node[0]][node[1]] == ".":
            full_grid[node[0]][node[1]] = "#"
    
    for row in full_grid:
        print("".join(row))

def part_one():
    with open("day08.txt", "r") as f:
        grid = [list(line.rstrip()) for line in f.readlines()]
    
    nrow = len(grid)
    ncol = len(grid[0])
    antennae = get_antenna_locations(grid)

    antinodes = set()

    for _, locations in antennae.items():
        pairs = itertools.combinations(locations, 2)
        for (a, b) in pairs:
            diff = (b[0] - a[0], b[1] - a[1])
            loc1 = (a[0] - diff[0], a[1] - diff[1])
            loc2 = (b[0] + diff[0], b[1] + diff[1])
            for loc in [loc1, loc2]:
                if 0 <= loc[0] < nrow and 0 <= loc[1] < ncol:
                    antinodes.add(loc)
    
    print_grid(grid, antinodes)
    print(f"Num antinodes = {len(antinodes)}")


def part_two():
    with open("day08.txt", "r") as f:
        grid = [list(line.rstrip()) for line in f.readlines()]
    
    nrow = len(grid)
    ncol = len(grid[0])
    antennae = get_antenna_locations(grid)

    antinodes = set()

    for _, locations in antennae.items():
        pairs = itertools.combinations(locations, 2)
        for (a, b) in pairs:
            diff = (b[0] - a[0], b[1] - a[1])

            node = a
            while 0 <= node[0] < nrow and 0 <= node[1] < ncol:
                antinodes.add(node)
                node = (node[0] - diff[0], node[1] - diff[1])
            
            node = b
            while 0 <= node[0] < nrow and 0 <= node[1] < ncol:
                antinodes.add(node)
                node = (node[0] + diff[0], node[1] + diff[1])
    
    print_grid(grid, antinodes)
    print(f"Num antinodes = {len(antinodes)}")

if __name__ == "__main__":
    part_one()
    part_two()