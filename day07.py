import itertools
from math import log10

def parse_input(fname):
    equations = []
    with open(fname, "r") as f:
        while line := f.readline():
            a, b = line.rstrip().split(":")
            target = int(a)
            nums = [int(x) for x in b.split()]
            equations.append((target, nums))
    return equations

def num_digits(x):
    return int(log10(x)) + 1

# Faster than built-in eval()
eval_fns = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "||": lambda x, y: x * 10 ** num_digits(y) + y
}

def meets_target(numbers, operators, target):
    result = numbers[0]
    for i, x in enumerate(numbers[1:]):
        op = operators[i]
        result = eval_fns[op](result, x)

        # Early stopping if we overshoot, since the only allowed operators
        # (+, *, concat) all increase the result
        if result > target:
            return False
    return result == target

def get_valid_equations(equations, allowed_ops):
    valid_equations = []
    for eqn in equations:
        target = eqn[0]
        nums = eqn[1]
        print(f"Testing {target} | {nums}")
        combos = list(itertools.product(allowed_ops, repeat=len(nums) - 1))
        
        for ops in combos:
            if meets_target(nums, ops, target):
                valid_equations.append((target, nums, ops))
                print("Valid")
                break
    return valid_equations


def part_one():
    equations = parse_input("input/day07.txt")
    valid_equations = get_valid_equations(equations, ["+", "*"])
    target_sum = sum([x[0] for x in valid_equations])
    
    print(f"Num valid equations = {len(valid_equations)}")
    print(f"Sum of targets = {target_sum}")

def part_two():
    equations = parse_input("input/day07.txt")
    valid_equations = get_valid_equations(equations, ["+", "*", "||"])
    target_sum = sum([x[0] for x in valid_equations])
    
    print(f"Num valid equations = {len(valid_equations)}")
    print(f"Sum of targets = {target_sum}")

if __name__ == "__main__":
    part_one()
    part_two()
