def expand_plot(start, grid):
    nrow = len(grid)
    ncol = len(grid[0])

    # Use BFS to find the full size of the plot
    # Area = total number of cells
    # Perimeter = 4 * total number of cells - 2 * unvisited adjacents added to queue
    area = 0
    perimeter = 0
    queue = [start]
    visited = set()

    while len(queue) > 0:
        node = queue.pop(0)
        if node in visited:
            continue

        letter = grid[node[0]][node[1]]
        visited.add(node)
        area += 1
        perimeter += 4

        for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            neighbour = (node[0] + d[0], node[1] + d[1])
            if (0 <= neighbour[0] < nrow and 0 <= neighbour[1] < ncol
                    and neighbour not in visited
                    and grid[neighbour[0]][neighbour[1]] == letter):
                queue.append(neighbour)
                perimeter -= 2

    return area, perimeter, visited

def get_corners(nodes):
    HALF_STEPS = [(-0.5, -0.5), (-0.5, 0.5), (0.5, 0.5), (0.5, -0.5)]

    corners = []
    for node in nodes:
        # Test all four corners of each node that makes up plot
        for x in HALF_STEPS:
            corner = (node[0] + x[0], node[1] + x[1])
            adjacents = []
            for y in HALF_STEPS:
                check = (int(corner[0] + y[0]), int(corner[1] + y[1]))
                if check in nodes:
                    adjacents.append(check)
                
            if len(adjacents) in (1, 3) and corner not in corners:
                # It's a corner of the plot if it touches an odd number of cells
                corners.append(corner)
            elif len(adjacents) == 2 and corner not in corners:
                # Interior corners are also created by two diagonally-opposed cells
                if all([adjacents[0][i] != adjacents[1][i] for i in range(2)]):
                    # This is the reason why corners is a list not a set
                    # We have to count these specific corners twice
                    corners.extend([corner] * 2)
    
    return corners


def part_one():
    with open("input/day12.txt", "r") as f:
        grid = [list(line.rstrip()) for line in f.readlines()]
    
    nrow = len(grid)
    ncol = len(grid[0])
    
    plots = []
    visited = set()
    for r in range(nrow):
        for c in range(ncol):
            node = (r, c)
            if node in visited:
                continue
            letter = grid[r][c]
            area, perimeter, nodes = expand_plot(node, grid)
            plots.append((letter, area, perimeter))
            visited.update(nodes)
    
    # print(plots)
    total_price = sum([p[1] * p[2] for p in plots])
    print(f"Total price = {total_price}")


def part_two():
    with open("input/day12.txt", "r") as f:
        grid = [list(line.rstrip()) for line in f.readlines()]
    
    nrow = len(grid)
    ncol = len(grid[0])
    
    plots = []
    visited = set()
    for r in range(nrow):
        for c in range(ncol):
            node = (r, c)
            if node in visited:
                continue
            letter = grid[r][c]
            area, _, nodes = expand_plot(node, grid)

            # From list of nodes that make up the plot, count corners
            # For a 2D shape, corners = sides
            corners = get_corners(nodes)
            plots.append((letter, area, len(corners)))
            visited.update(nodes)
    
    # print(plots)
    total_price = sum([p[1] * p[2] for p in plots])
    print(f"Total price = {total_price}")

if __name__ == "__main__":
    part_one()
    part_two()