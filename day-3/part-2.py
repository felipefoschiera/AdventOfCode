
groups = []
cur_group = []

with open('input', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        
        cur_group.append(line)
        if len(cur_group) == 3:
            groups.append(cur_group)
            cur_group = []

sum_priorities = 0

for group in groups:
    common_char = ''
    present_count = {}
    for line in group:
        unique = set(line)
        for char in unique:
            if char not in present_count:
                present_count[char] = 1
            else:
                	present_count[char] += 1

    for c in present_count:
        if present_count[c] == 3:
            common_char = c

    if common_char.isupper():
        priority = 26 + ord(common_char) - ord('A') + 1
    else:
        priority = ord(common_char) - ord('a') + 1
    sum_priorities += priority

print(sum_priorities)
