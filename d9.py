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

def generate_tree(history):
    history.append(diff(history[-1]))
    if history[-1].count(history[-1][0]) == len(history[-1]):
        for i in range(len(history)-1, 0, -1):
            history[i-1].insert(0, (history[i-1][0] - history[i][0]))
            history[i-1].append(history[i][-1] + history[i-1][-1])
        return history[0][-1], history[0][0]
    else:
        return generate_tree(history)

for line in file:
   part1, part2 = generate_tree(line)
   tot1 += part1
   tot2 += part2

print(tot1)
print(tot2)

    