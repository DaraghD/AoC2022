from dataclasses import dataclass
@dataclass
class elf_file:
    name: str
    size: int
    subfile: list

@dataclass
class elf_dir:
    name: str
    size: int
    subdir: list

dir_path = []
directory = []

with open("test.txt") as file:
    line = [line for line in file]

for command in line:
    if dir_path:
        current_dir = dir_path[-1]
    com_temp = command.split(" ")
    if "cd /" in command:
        home = elf_dir("home", 0, [])
        dir_path.append(home)
        directory.append(home)
    elif "cd .." in command:
        dir_path.pop()
    elif com_temp[0].isdigit():  # file with a size
        value = int(com_temp[0])
        current_dir.subdir.append(elf_file(com_temp[1], value, []))
    elif "cd" in command:
        new_dir = elf_dir(com_temp[2], 0, [])
        current_dir.subdir.append(new_dir)
        dir_path.append(new_dir)
    else:
        continue

def find_size(edir: elf_dir):  #if a/e has i , e value = i , but a value = e value and i value , counting files like these twice
    total = 0
    for i in range(len(edir.subdir)):
        if type(edir.subdir[i]) == elf_dir:  # see if its a directory
            if edir.subdir[i].size == 0:
                total += find_size(edir.subdir[i])
            else:
                total += edir.subdir[i].size
    else:
        for i in range(len(edir.subdir)):
            total += edir.subdir[i].size
        else:
            edir.size = total

    return total

directory[0].size = find_size(directory[0])
print(directory[0].size)
