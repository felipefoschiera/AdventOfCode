# check whether a_seg fully contains b_seg
def fully_contains(a_seg, b_seg):
    a_start, a_end = list(map(int, a_seg.split('-')))
    b_start, b_end = list(map(int, b_seg.split('-')))

    return b_start >= a_start and b_end <= a_end

# check whether a_seg and b_seg overlap
def overlaps(a_seg, b_seg):
    a_start, a_end = list(map(int, a_seg.split('-')))
    b_start, b_end = list(map(int, b_seg.split('-')))

    # a: [1, 10]
    # b: [8, 15]

    biggest_start = max(a_start, b_start)
    earliest_end = min(a_end, b_end)

    overlapped = max(0, (earliest_end - biggest_start) + 1)

    return overlapped > 0

pairs_fully_contains = 0
pairs_overlap = 0

with open('input', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        a, b = line.split(',')

        if fully_contains(a, b) or fully_contains(b, a):
            pairs_fully_contains += 1
        if overlaps(a, b):
            pairs_overlap += 1

print(pairs_fully_contains)
print(pairs_overlap)