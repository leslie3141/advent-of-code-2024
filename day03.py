import re

def part_one():
    with open("day03.txt", "r") as f:
        data = f.read()
    
    matches = re.findall(r"mul\(\d+,\d+\)", data)
    tot = 0
    for m in matches:
        print(m)
        a, b = re.match(r"mul\((\d+),(\d+)\)", m).groups()
        tot += int(a) * int(b)
    
    print(f"total = {tot}")

def part_two():
    with open("day03.txt", "r") as f:
        data = f.read()
    
    matches = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", data)
    tot = 0
    enabled = True
    for m in matches:
        print(m)
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        else:
            a, b = re.match(r"mul\((\d+),(\d+)\)", m).groups()
            if enabled:
                tot += int(a) * int(b)
    
    print(f"total = {tot}")

if __name__ == "__main__":
    part_two()
