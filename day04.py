def count_matches(word, grid):
    first_char = word[0]
    nchar = len(word)
    nrow = len(grid)
    ncol = len(grid[0])
    print(f"{nrow} x {ncol} grid")

    DIRECTIONS = [(0, 1), (1, 1), (1, 0), (1, -1),
                  (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    tot_matches = 0
    for r in range(nrow):
        for c in range(ncol):
            if grid[r][c] != first_char:
                continue
            
            for d in DIRECTIONS:
                if ((not -1 <= r + nchar * d[0] <= nrow) or
                        (not -1 <= c + nchar * d[1] <= ncol)):
                    continue

                check = "".join([grid[r + i * d[0]][c + i * d[1]] for i in range(nchar)])
                if check == word:
                    tot_matches += 1
                    print(f"match at ({r}, {c}) in dir {d}")
    
    return tot_matches

def count_xmas(word, grid):
    nchar = len(word)
    mid_idx = nchar // 2
    mid_char = word[mid_idx]
    reversed = word[::-1]

    nrow = len(grid)
    ncol = len(grid[0])
    print(f"{nrow} x {ncol} grid")

    tot_xmas = 0
    for r in range(mid_idx, nrow - mid_idx):
        for c in range(mid_idx, ncol - mid_idx):
            if grid[r][c] != mid_char:
                continue

            word1 = "".join([grid[r - mid_idx + i][c - mid_idx + i] for i in range(nchar)])
            word2 = "".join([grid[r + mid_idx - i][c - mid_idx + i] for i in range(nchar)])

            if word1 in (word, reversed) and word2 in (word, reversed):
                tot_xmas += 1
                print(f"xmas centred on ({r}, {c})")


    return tot_xmas

def part_one():
    with open("day04.txt", "r") as f:
        grid = [list(line.rstrip()) for line in f.readlines()]
    
    num_matches = count_matches("XMAS", grid)
    print(f"matches = {num_matches}")

def part_two():
    with open("day04.txt", "r") as f:
        grid = [list(line.rstrip()) for line in f.readlines()]
    
    num_xmas = count_xmas("MAS", grid)
    print(f"xmas = {num_xmas}")


if __name__ == "__main__":
    part_two()
