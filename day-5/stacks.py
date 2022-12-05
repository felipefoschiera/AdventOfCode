readInitial = True
multiMove = True

stack_lines = []
moves = []
with open('input', 'r') as f:
    for line in f.readlines():
        line = line.split('\n')[0]
        if line == '':
            readInitial = False
            continue
        if readInitial:
            stack_lines.append(line)
        else:
            _, quantity, _, initial_stack, _, dest_stack = line.split()
            moves.append((quantity, initial_stack, dest_stack))

num_stacks = stack_lines.pop().split()[-1]
num_stacks = int(num_stacks)

stacks = [[] for _ in range(num_stacks)]

for line in stack_lines:
    for stack_idx in range(num_stacks):
        val = line[stack_idx * 4 + 1]
        stacks[stack_idx].append(val)

for i in range(num_stacks):
    stacks[i] = stacks[i][::-1]
    stacks[i] = (' '.join(stacks[i])).split()

for move in moves:
    quant, initial, dest = map(int, move)
    if multiMove == False:
        for i in range(quant):
            val = stacks[initial-1].pop()
            stacks[dest-1].append(val)
    else:
        vals = []
        for i in range(quant):
            val = stacks[initial-1].pop()
            vals.append(val)
        vals.reverse()
        stacks[dest-1].extend(vals)

ans = ""
for stack in stacks:
    ans += stack[-1]
print(ans)