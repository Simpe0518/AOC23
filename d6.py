import itertools
file = open("d6.txt", "r")
file = [line for line in file]


t1 = [int(l) for l in  file[0].split()[1:]]
d1 = [int(l) for l in  file[1].split()[1:]]

t2 = int("".join([l for l in  file[0].split()[1:]]))
d2 = int("".join([l for l in  file[1].split()[1:]]))


records = 0
tot = 1

### part 1 ###
for (t,d) in zip(t1, d1):
    for i in range(t):
        if i*(t-i) > d:
            records += 1

    tot *= records
    records = 0
print(tot)

### part 2 ###

for i in range(t2):
    if i*(t2-i) > d2:
        records += 1
print(records)

        