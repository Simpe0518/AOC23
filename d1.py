from asyncio.windows_events import NULL

file = open("d1.txt", "r")
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

first = NULL
last = NULL
tot = 0
for line in file.readlines():
    print(line)
    for digit in range(len(numbers)):
        line = line.replace(numbers[digit],  numbers[digit] + str(digit+1) + numbers[digit])
    print(line)

    for i in line:
        if (i.isdigit()):
            last = i
            if (first == NULL):
                first = i
        
    tot += int(str(first) + str(last))
    first = NULL

print(tot)
        
