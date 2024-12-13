from collections import defaultdict
from functools import cmp_to_key

def parse_input(fname):
    rules = defaultdict(list)
    books = []
    with open(fname, "r") as f:
        while line := f.readline():
            line = line.rstrip()
            if "|" in line:
                # Rules is a dict where keys are "before" pages and vals
                # are lists of all "after" pages
                a, b = [int(x) for x in line.split("|")]
                rules[a].append(b)
            elif "," in line:
                books.append([int(x) for x in line.split(",")])
    
    return rules, books

def book_is_valid(book, rules):
    for i, p in enumerate(book):
        followers = rules[p]
        if any([x in followers and x in book and x not in book[i + 1:]
                for x in followers]):
            return False
    
    return True

def compare_pages(p1, p2, rules):
    #' Custom compare function for comparing two pages for sequencing
    #' Required for custom sorting of pages in books
    #' Sort order based on sequencing rules dictionary - if p2 must come after p1,
    #' return -1. If p1 must come after p2, return 1. Else return 0.
    if p2 in rules[p1]:
        return -1
    elif p1 in rules[p2]:
        return 1
    else:
        return 0


def part_one():
    rules, books = parse_input("day05.txt")

    valid_books = [b for b in books if book_is_valid(b, rules)]
    
    print(f"tot books = {len(books)}, valid books = {len(valid_books)}")
    sum_mid_pages = sum([b[len(b) // 2] for b in valid_books])
    print(f"sum mid pages = {sum_mid_pages}")


def part_two():
    rules, books = parse_input("day05.txt")

    invalid_books = []
    for book in books:
        if not book_is_valid(book, rules):
            # Sort using our custom page compare function and cmp_to_key
            sorted_book = sorted(book, key=cmp_to_key(lambda x, y: compare_pages(x, y, rules)))
            invalid_books.append(sorted_book)
    
    print(f"tot books = {len(books)}, invalid books = {len(invalid_books)}")
    sum_mid_pages = sum([b[len(b) // 2] for b in invalid_books])
    print(f"sum mid pages = {sum_mid_pages}")


if __name__ == "__main__":
    part_one()
    part_two()
