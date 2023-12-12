file = open("d9.txt", "r")
file = [[[int(c) for c in line.strip("").split()]] for line in file]

tot1 = 0
tot2 = 0
history = []

def diff(history):
    new = []
    for i in range(1, len(history)):
        new.append(history[i] - (history[i-1]))
    return new

### part 1 ###
def generate_tree1(history):
    history.append(diff(history[-1]))
    if history[-1].count(history[-1][0]) == len(history[-1]):
        for i in range(len(history)-1, 0, -1):
            history[i-1].append(history[i][-1] + history[i-1][-1])
        return history[0][-1]
    else:
        return generate_tree1(history)
    
### part 2 ###
def generate_tree2(history):
    history.append(diff(history[-1]))
    if history[-1].count(history[-1][0]) == len(history[-1]):
        for i in range(len(history)-1, 0, -1):
            history[i-1].insert(0, (history[i-1][0] - history[i][0]))
        return history[0][0]
    else:
        return generate_tree2(history)

for line in file:
   tot1 += generate_tree1(line)
   tot2 += generate_tree2(line)

print(tot1)
print(tot2)

    