file = open("d14.txt", "r")
file = [[c for c in line.strip()] for line in file]

def rock_ahead(file, r, c):
    if file[r-1][c] == "O" or file[r-1][c] == "#" or r == 0:
        return True
    return False
    
def move_rock(file, r ,c):
    if not rock_ahead(file, r, c ):
        file[r][c] = "."
        return move_rock(file , r-1, c)
    else:
        file[r][c] = "O"
        return file

def fall_north(file):
    for r in range(1, len(file)):
        for c in range(len(file[r])):
            if file[r][c] == "O":
                file = move_rock(file, r, c)
    return file

def count_rock(file):
    tot = 0
    for r in range(len(file)):
        tot += file[r].count("O") * (len(file) - r)
    return tot


file = fall_north(file)
for line in file:
    print("".join(line).strip())

print(count_rock(file))