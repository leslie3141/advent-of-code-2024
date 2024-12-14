def input_to_blocks(input):
    #' Returns list of individual blocks
    blocks = []
    for i, c in enumerate(input):
        if i % 2:
            # odds - empty blocks
            blocks.extend(["."] * int(c))
        else:
            # evens - id nums
            blocks.extend([i // 2] * int(c))
    return blocks

def input_to_files(input):
    #' Returns list of files as tuples (id, size)
    blocks = []
    for i, c in enumerate(input):
        if i % 2:
            # odds - empty blocks
            blocks.append((".", int(c)))
        else:
            # evens - id nums
            blocks.append((i // 2, int(c)))
    return blocks

def files_to_blocks(files):
    #' Converts a list of files to a list of raw blocks
    blocks = []
    for (id, size) in files:
        blocks.extend([id] * size)
    return blocks

def checksum(blocks):
    #' Calculates checksum of a list of blocks
    return sum([i * x for i, x in enumerate(blocks) if x != "."])

def part_one():
    with open("day09.txt", "r") as f:
        input = f.read().rstrip()

    # input = "2333133121414131402"
    blocks = input_to_blocks(input)
    # print("".join([str(c) for c in blocks]))

    # two indices - one from start, one from end
    # index from start stops whenever there's an empty block, and
    # then the index from the end looks for a non-empty block. then the
    # blocks are swapped. this continues until start index > end index
    i = 0
    j = len(blocks) - 1
    while i < j:
        # Look for next empty block from start
        while i < j and blocks[i] != ".":
            i += 1
        # Look for next non-empty block from end
        while i < j and blocks[j] == ".":
            j -= 1
        # Swap elements
        blocks[i], blocks[j] = blocks[j], blocks[i]
    
    # print("".join([str(c) for c in blocks]))
    print(checksum(blocks))

def part_two():
    with open("day09.txt", "r") as f:
        input = f.read().rstrip()

    # input = "2333133121414131402"
    files = input_to_files(input)

    # if block fits - insert two blocks in place; one with actual file, another
    # blank block padded out to match size of OG block (if needed)
    # put a blank block in place of original file location
    curr_id = None
    i = len(files) - 1
    while i > 0:
        (id, size) = files[i]
        # Skip empty blocks and files already tested
        if id == "." or (curr_id is not None and id > curr_id):
            i -= 1
            continue

        curr_id = id
        # Find first available empty space that fits current file
        for j in range(i):
            (j_id, j_size) = files[j]
            if j_id == "." and j_size >= size:
                # Delete OG file and replace with empty space
                del files[i]
                files.insert(i, (".", size))
                # Insert file + optional empty space into located empty space
                del files[j]
                files.insert(j, (id, size))
                if j_size > size:
                    files.insert(j + 1, (".", j_size - size))
                
                break
        i -= 1
    
    blocks = files_to_blocks(files)
    # print("".join([str(c) for c in blocks]))
    print(checksum(blocks))

if __name__ == "__main__":
    part_one()
    part_two()
