calories = []
current_sum = 0

with open('input', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if line == '':
            calories.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)

calories.append(current_sum)

calories.sort()

# Part 1
print(calories[-1])

# Part 2
print(sum(calories[-3:]))