from enum import Enum

class CommandType(Enum):
    LIST = 1
    CD_DIR = 2
    CD_BACK = 3
    CD_ROOT = 4

def read_lines(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            lines.append(line)
    return lines, len(lines)

def is_command(line):
    return line[0] == '$'

def get_command_parameter(line):
    elements = line.split()
    return elements[2]

def find_command_type(line):
    elements = line.split()
    command = elements[1]

    if command == "ls":
        return CommandType.LIST

    if command == "cd":
        parameter = elements[2]
        if parameter == "..":
            return CommandType.CD_BACK
        if parameter == "/":
            return CommandType.CD_ROOT

    return CommandType.CD_DIR

lines, total_lines = read_lines('input')

    
pointer = 0
directory_stack = []

def get_directory_path(cur_stack):
    return '/'.join(cur_stack)

folder_files = {}
folder_adjacency = {}

while pointer < total_lines:
    line = lines[pointer]
    if is_command(line):
        command_type = find_command_type(line)
        
        if command_type == CommandType.CD_ROOT:
            directory_stack.clear()
            directory_stack.append("/")
            pointer += 1
            continue

        if command_type == CommandType.CD_DIR:
            parameter = get_command_parameter(line)
            directory_stack.append(parameter)
            pointer += 1
            continue

        if command_type == CommandType.CD_BACK:
            directory_stack.pop()
            pointer += 1
            continue

        if command_type == CommandType.LIST:
            pointer += 1
            dir_contents = []
            while pointer < total_lines and not is_command(lines[pointer]):
                dir_contents.append(lines[pointer])
                pointer += 1

            dir_path = get_directory_path(directory_stack)
            folders = []
            files = []
            for content in dir_contents:
                a, b = content.split()
                if a == "dir":
                    folders.append(b) # folder name
                else:
                    files.append(int(a)) # size

            folder_files[dir_path] = files


            for folder in folders:
                folder_path = dir_path + '/' + folder
                if not dir_path in folder_adjacency:
                    folder_adjacency[dir_path] = [folder_path]
                else:
                    folder_adjacency[dir_path].append(folder_path)

visited = {}
folder_sizes = {}

def dfs(folder):
    folder_size = 0
    visited[folder] = True
    if folder in folder_adjacency:
        for child in folder_adjacency[folder]:
            if child not in visited:
                folder_size += dfs(child)

    folder_size += sum(folder_files[folder])
    folder_sizes[folder] = folder_size
    return folder_size

dfs('/')

up_to_100k_sum = 0
for folder in folder_sizes:
    size = folder_sizes[folder]
    if size <= 100000:
        up_to_100k_sum += size

# print(up_to_100k_sum)

## Part 2

total_disk_space = 70000000
needed = 30000000
current_used = folder_sizes['/']

unused_space = total_disk_space - current_used
missing_space = needed - unused_space

all_folder_sizes = [folder_sizes[folder] for folder in folder_sizes]
all_folder_sizes.sort()

for size in all_folder_sizes:
    if size >= missing_space:
        print(size)
        break