def parse_input(fname):
    starts = []
    grid = []
    with open(fname, "r") as f:
        for r, line in enumerate(f.readlines()):
            tiles = [int(x) for x in line.rstrip()]
            grid.append(tiles)
            starts.extend([(r, c) for c, x in enumerate(tiles) if x == 0])

    return starts, grid

def get_trailhead_score(start, grid, rating):
    # Use a BFS to find all possible 9s reachable from a given tile
    nrow = len(grid)
    ncol = len(grid[0])
    visited = set()
    queue = [start]

    score = 0
    while len(queue) > 0:
        tile = queue.pop(0)
        # Skip visited tiles if we're calculating score instead of rating
        # i.e. don't care about distinct paths
        if tile in visited and not rating:
            continue

        height = grid[tile[0]][tile[1]]
        visited.add(tile)

        if height == 9:
            # Increment score if we reach a 9
            score += 1
        else:
            # Otherwise add all adjacents that increase by 1
            for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_tile = (tile[0] + d[0], tile[1] + d[1])
                if 0 <= next_tile[0] < nrow and 0 <= next_tile[1] < ncol:
                    if grid[next_tile[0]][next_tile[1]] == height + 1:
                        queue.append(next_tile)

    return score


def part_one():
    starts, grid = parse_input("day10.txt")
    scores = [get_trailhead_score(s, grid, False) for s in starts]
    print(f"Total trailhead score = {sum(scores)}")

def part_two():
    starts, grid = parse_input("day10.txt")
    ratings = [get_trailhead_score(s, grid, True) for s in starts]
    print(f"Total trailhead rating = {sum(ratings)}")

if __name__ == "__main__":
    part_one()
    part_two()
