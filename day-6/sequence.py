def is_all_different(sequence):
    return len(sequence) == len(set(sequence))

def solve(num_chars):
    line = None
    with open('input', 'r') as f:
        line = f.readline()
    
    cur_seq = []

    for i in range(len(line)):
        if i <= num_chars - 1:
            cur_seq.append(line[i])
            continue
        cur_seq.pop(0)
        cur_seq.append(line[i])
        
        if len(cur_seq) == num_chars and is_all_different(cur_seq):
            return i + 1

print(solve(4), solve(14))