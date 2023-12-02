import math
tot_games = 0
tot_cubes = 0
colors = {"red": 12,"green": 13,"blue": 14}
cubes = {"red": 0,"green": 0,"blue": 0}

file = open("d2.txt", "r")

for line in file:
    valid = True
    line = line.split()
    for i in range(len(line)):
        c = [c for c in colors.keys() if c in line[i]]
        if  c:
            c = c[0]
            n = int(line[i-1])
            if colors[c] < n:     
                valid = False
            if  cubes[c] < n:
                    cubes[c] = n
            
    if valid:
        tot_games += int(line[1].strip(":"))
    tot_cubes += math.prod(cubes.values())
    cubes = dict.fromkeys(cubes, 0)
        
print(tot_games)
print(tot_cubes)
