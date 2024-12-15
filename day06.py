import copy

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def fill_visited_squares(g, start_r, start_c):
    grid = copy.deepcopy(g)
    nrow = len(grid)
    ncol = len(grid[0])

    r, c = (start_r, start_c)
    di = 0
    d = DIRECTIONS[di]

    while True:
        grid[r][c] = "X"

        if not ((0 <= r + d[0] < nrow) and (0 <= c + d[1] < ncol)):
            # we've reached the end
            break
        else:
            next_tile = grid[r + d[0]][c + d[1]]
            # if we're facing an obstacle, rotate
            if next_tile == "#":
                di = (di + 1) % len(DIRECTIONS)
                d = DIRECTIONS[di]
            else:
                # then move forward one step
                r += d[0]
                c += d[1]
    
    return grid


def part_one():
    with open("input/day06.txt", "r") as f:
        grid = [list(line.rstrip()) for line in f.readlines()]
    
    nrow = len(grid)
    ncol = len(grid[0])
    print(f"{nrow} x {ncol} grid")

    # Get starting position
    for i, row in enumerate(grid):
        if "^" in row:
            start_r = i
            start_c = row.index("^")
            break
    
    print(f"Starting position: ({start_r}, {start_c})")

    filled = fill_visited_squares(grid, start_r, start_c)

    tot_visited = sum([row.count("X") for row in filled])
    print(f"Total spaces visited = {tot_visited}")


def part_two():
    with open("input/day06.txt", "r") as f:
        grid = [list(line.rstrip()) for line in f.readlines()]
    
    nrow = len(grid)
    ncol = len(grid[0])
    print(f"{nrow} x {ncol} grid")

    # Get starting position
    for i, row in enumerate(grid):
        if "^" in row:
            start_r = i
            start_c = row.index("^")
            break
    
    print(f"Starting position: ({start_r}, {start_c})")
    filled = fill_visited_squares(grid, start_r, start_c)

    placements = []

    for test_r in range(nrow):
        for test_c in range(ncol):
            # Only test spaces on original path - as these are the only spaces
            # where obstructions can affect the route
            if filled[test_r][test_c] != "X" or (test_r, test_c) == (start_r, start_c):
                continue

            print(f"Testing ({test_r}, {test_c})")
            test_grid = copy.deepcopy(grid)
            test_grid[test_r][test_c] = "#"

            r, c = (start_r, start_c)
            di = 0
            d = DIRECTIONS[di]

            visited = set()

            while True:
                if (r, c, di) in visited:
                    placements.append((test_r, test_c))
                    print("This placement results in a loop")
                    print(f"Revisiting {(r, c, di)}")
                    break

                # visited.add((r, c, di))
                if not ((0 <= r + d[0] < nrow) and (0 <= c + d[1] < ncol)):
                    # we've reached the end
                    break
                else:
                    next_tile = test_grid[r + d[0]][c + d[1]]
                    if next_tile == "#":
                        # if we're facing an obstacle, rotate
                        visited.add((r, c, di))
                        di = (di + 1) % len(DIRECTIONS)
                        d = DIRECTIONS[di]
                    else:
                        # otherwise, move forward one step
                        r += d[0]
                        c += d[1]

    print(f"Num valid placements = {len(placements)}")

if __name__ == "__main__":
    part_two()
