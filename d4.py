import math
file = open("d4.txt", "r")
file = [line for line in file]

winning_nr = []
elf_nr = []
our_nr = False
winns = 0
tot = 0
tot_2 = 0


for line in file:
    line = line.split()
    for c in line[2:]:
        if c == "|":
            our_nr = True
        else: 
            if not our_nr:
                winning_nr.append(int(c))
            else:
                elf_nr.append(int(c))
    our_nr = False
    
    winns = len(set(winning_nr) & set(elf_nr))
    if winns:
        tot += 2**(winns-1)
    elf_nr = []
    winning_nr = []



for card in file:
    line = card.split()
    for c in line[2:]:
        if c == "|":
            our_nr = True
        else: 
            if not our_nr:
                winning_nr.append(int(c))
            else:
                elf_nr.append(int(c))
    our_nr = False
    
    for x in range(len(set(winning_nr) & set(elf_nr))):
        file.insert(, file[int(line[1].strip(":"))-1+x])
        
    elf_nr = []
    winning_nr = []

print("")