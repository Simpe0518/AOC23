from sys import setrecursionlimit
from math import gcd
setrecursionlimit(25000)

file = open("d8.txt", "r")
file = [line for line in file]

directions = file.pop(0).strip()
file.pop(0)
paths = {}


for l in file:
    l = l.split()
    paths[l[0]] = [l[2].strip(",").strip("("), l[3].strip(")")]

#part 1
def find1(start, end, d, cntr = 0):

    if start in end:
        return cntr
    cntr += 1
    return find1(paths[start][0 if d[0] == "L" else 1], end, d[1:]+d[0], cntr)

#part 2
start_nodes = [n for n in paths.keys() if n[2] == "A"]
end_nodes = [n for n in paths.keys() if n[2] == "Z"]
cntr = 1
first = []


for n in start_nodes:
    first.append(find1(n, end_nodes, directions))

for i in first:
        cntr = cntr*i//gcd(cntr,i)

print(find1("AAA", ["ZZZ"], directions))
print(cntr)

    
        

        
