from collections import defaultdict

def part_one():
    list1 = []
    list2 = []

    with open("input/day01.txt", "r") as f:
        while line := f.readline():
            a, b = [int(x) for x in line.rstrip().split()]
            list1.append(a)
            list2.append(b)

    list1.sort()
    list2.sort()

    tot_diff = sum([abs(a - b) for a, b in zip(list1, list2)])
    print(tot_diff)

def part_two():
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    with open("input/day01.txt", "r") as f:
        while line := f.readline():
            a, b = [int(x) for x in line.rstrip().split()]
            dict1[a] += 1
            dict2[b] += 1

    score = sum([x * dict1[x] * dict2[x] for x in dict1.keys()])
    print(score)

if __name__ == "__main__":
    part_one()
    part_two()
