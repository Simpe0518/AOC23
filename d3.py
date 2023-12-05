import re
file = open("d3.txt", "r")

schema = [line for line in file]
number = ""
tot = 0

def has_adjecant(r, c, l, number):



    


    """if r == len(schema[r][c]):
        if (schema[r][c-l-1:c] + schema[r-1][c-l-1:c] + schema[r+1][c-l-1:c]).count(".") != l*2 + 3:
            return False

    if r == 0:
        if (schema[r][c-l:c+1] + schema[r-1][c-l:c+1] + schema[r+1][c-l:c+1]).count(".") != l*2 + 3:
            return False

    if (schema[r][c-l-1:c+1] + schema[r-1][c-l-1:c+1] + schema[r+1][c-l-1:c+1]).count(".") != l*2 + 6:
        return False
    return True"""

        
    


for r in range(len(schema)):
    for c in range(len(schema[r])):
        if schema[r][c].isdigit():
            number += schema[r][c]
        if schema[r][c] == "." and number:
            if has_adjecant(r, c, len(number), number):
                tot += int(number)
print(tot)


    


