from collections import Counter, defaultdict
from math import log10

def num_digits(x):
    return int(log10(x)) + 1

def iterate(stones):
    #' Naive approach which goes through each stone individually
    new_list = []
    for s in stones:
        if s == 0:
            new_list.append(1)
        else:
            nd = num_digits(s)
            if nd % 2 == 0:
                div = 10 ** int(nd / 2)
                new_list.append(s // div)
                new_list.append(s % div)
            else:
                new_list.append(s * 2024)
    return new_list

def iterate_better(stones):
    #' Using a dict which tracks occurrences of each number in list
    #' Since there will be lots of duplicates (e.g. 0, 1, 2024)
    #' Allows us to calculate many stones at a time
    new_list = defaultdict(int)
    for val, count in stones.items():
        if val == 0:
            new_list[1] += count
        else:
            nd = num_digits(val)
            if nd % 2 == 0:
                div = 10 ** int(nd / 2)
                new_list[val // div] += count
                new_list[val % div] += count
            else:
                new_list[val * 2024] += count
    return new_list

def part_one():
    with open("input/day11.txt", "r") as f:
        stones = [int(x) for x in f.read().rstrip().split()]

    for i in range(30):
        stones = iterate(stones)
        print(f"Iteration {i + 1}: {len(stones)} stones")

def part_two():
    with open("input/day11.txt", "r") as f:
        stones_list = [int(x) for x in f.read().rstrip().split()]

    stones = Counter(stones_list)

    for i in range(75):
        stones = iterate_better(stones)
        tot_stones = sum([c for c in stones.values()])
        print(f"Iteration {i + 1}: {tot_stones} stones")

if __name__ == "__main__":
    part_one()
    part_two()
