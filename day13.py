import numpy as np
from numpy.linalg import inv
import re

class Machine:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize
    
    def solve_presses(self):
        # Can be solved as a system of two linear equations
        # Ax = b --> x = A'b
        # Note this assumes a and b don't have the same direction
        A = np.array([[self.a[0], self.b[0]],
                      [self.a[1], self.b[1]]])
        target = np.array([self.prize[0], self.prize[1]])
        x = inv(A) @ target

        a_presses, b_presses = [round(i) for i in x]

        # Recheck to account for floating point error
        if all(A @ np.array([a_presses, b_presses]) == target):
            self.a_presses = a_presses
            self.b_presses = b_presses
            self.solvable = True
        else:
            self.solvable = False

        return self.solvable
    
    def has_solution(self):
        return self.solvable
        
    def retrieve_solution(self):
        return (self.a_presses, self.b_presses)
    
    def get_num_tokens(self):
        return 3 * self.a_presses + self.b_presses
    
    def inflate_prize(self):
        self.prize = [self.prize[i] + 10000000000000 for i in range(2)]


def parse_input(fname):
    machines = []
    with open(fname, "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
        
        for x in [lines[i:i + 4] for i in range(0, len(lines), 4)]:
            matches = [re.search(r"X[+=](\d+), Y[+=](\d+)", l) for l in x[:3]]
            a, b, prize = [(int(m.group(1)), int(m.group(2))) for m in matches]
            machines.append(Machine(a, b, prize))
    return machines

def part_one():
    machines = parse_input("input/day13.txt")
    for m in machines:
        if m.solve_presses():
            print(f"Solvable! Solution = {m.retrieve_solution()}")
        else:
            print("Impossible :(")

    tot_tokens = sum([m.get_num_tokens() for m in machines if m.has_solution()])
    print(f"Total tokens = {tot_tokens}")


def part_two():
    machines = parse_input("input/day13.txt")
    for m in machines:
        m.inflate_prize()
        if m.solve_presses():
            print(f"Solvable! Solution = {m.retrieve_solution()}")
        else:
            print("Impossible :(")

    tot_tokens = sum([m.get_num_tokens() for m in machines if m.has_solution()])
    print(f"Total tokens = {tot_tokens}")

if __name__ == "__main__":
    part_one()
    part_two()