file = open("d15.txt", "r")
file = file.read().strip().split(",")

tot1 = 0
tot2 = 0
boxes = {}

for i in range(256):
    boxes[i] = {}

def eval(line):
    cv = 0
    for c in line:
        cv += ord(c)
        cv *= 17
        cv = cv % 256
    return cv

#part 1
for line in file:
    tot1 += eval(line)

#part 2
for line in file:
    if "-" in line:
        label = line[:line.index("-")]
        fl = line[line.index("-")+1:]
        box_nr = eval(line[:line.index("-")])
        if label in boxes[box_nr].keys():
            boxes[box_nr].pop(label)

    if "=" in line:
        label = line[:line.index("=")]
        fl = line[line.index("=")+1:]
        box_nr = eval(label)
        boxes[box_nr][label] = fl

for box_nr, box in enumerate(boxes.values()):
    for slot, lens in enumerate(box.values()):
        tot2 += (box_nr+1) * (slot+1) * (int(lens))



#print(boxes)
print(tot1)
print(tot2)

    