import copy

def report_is_safe(L, low=1, high=3):
    safe_inc = all([low <= (x - y) <= high for x, y in zip(L, L[1:])])
    safe_dec = all([low <= (y - x) <= high for x, y in zip(L, L[1:])])
    print(f"list = {L}, inc = {safe_inc}, dec = {safe_dec}")
    return (safe_inc or safe_dec)

def report_is_almost_safe(L, low=1, high=3):
    safe_inc = [low <= (x - y) <= high for x, y in zip(L, L[1:])]
    safe_dec = [low <= (y - x) <= high for x, y in zip(L, L[1:])]
    
    if (all(safe_inc) or all(safe_dec)):
        return True
    elif sum(safe_inc) >= len(L) - 3 or sum(safe_dec) >= len(L) - 3:
        print(f"ALMOST SAFE - {L}")
        
        if sum(safe_inc) >= len(L) - 3:
            idx = safe_inc.index(False)
            if subreport_is_safe(L, idx, low, high) or subreport_is_safe(L, idx + 1, low, high):
                return True

        if sum(safe_dec) >= len(L) - 3:
            idx = safe_dec.index(False)
            if subreport_is_safe(L, idx, low, high) or subreport_is_safe(L, idx + 1, low, high):
                return True
    else:
        print(f"NOT SAFE - {L}")
    
    return False

def subreport_is_safe(L, idx, low=1, high=3):
    new_list = copy.deepcopy(L)
    new_list.pop(idx)
    return report_is_safe(new_list, low, high)

def part_one():
    count = 0
    with open("day02.txt", "r") as f:
        while line := f.readline():
            report = [int(x) for x in line.rstrip().split()]
            if report_is_safe(report, 1, 3):
                print("Safe")
                count += 1
            else:
                print("Unsafe")
    
    print(count)

def part_two():
    count = 0
    with open("day02.txt", "r") as f:
        while line := f.readline():
            report = [int(x) for x in line.rstrip().split()]
            if report_is_almost_safe(report, 1, 3):
                # print("Safe")
                count += 1
            else:
                # print("Unsafe")
                pass
    
    print(count)

if __name__ == "__main__":
    part_two()
