sum_priorities = 0

with open('input', 'r') as f:
    for line in f.readlines():
        line = line.strip()

        half = len(line) // 2
        part1 = line[:half]
        part2 = line[half:]

        item_present = {}

        for char in part1:
            item_present[char] = 1
        
        common_char = ''
        for char in part2:
            if char in item_present:
                common_char = char
        
        priority = 0

        if common_char.isupper():
            priority = 26 + ord(common_char) - ord('A') + 1
        else:
            priority = ord(common_char) - ord('a') + 1
        sum_priorities += priority

print(sum_priorities)