file = open("d14.txt", "r")
file = [[c for c in line.strip()] for line in file]
beam_loads = []
cntr = 0

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

#--- part 1 ---
print(count_rock(fall_north(file)))

#--- part 2 ---
while(True):
    for i in range(4):
        file = fall_north(file)
        rotat = list(zip(*reversed(file)))
        file = [list(line) for line in rotat]

    load = count_rock(file)
    cntr += 1

    if load in beam_loads:
        beam_loads = beam_loads[beam_loads.index(load):]
        l = len(beam_loads)
        print(beam_loads[(1000000000 - cntr) % l])
        break

    beam_loads.append(load)
