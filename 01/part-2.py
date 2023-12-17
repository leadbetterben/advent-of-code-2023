from re import search
from numpy import argmin, argmax

file = open("01/input.txt", "r")
result = 0
numNames = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numMappings = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for line in file.readlines():
    line = line.rstrip("\n")
    digits = [(i, c) for i, c in enumerate(line) if c.isdigit()]

    for numName in numNames:
        found = search(numName, line)
        if (found):
            digits.append((found.start(), numName))
    
    positions = []
    vals = []
    for tup in digits:
        positions.append(tup[0])
        val = tup[1]
        if val in numNames:
            val = numMappings[val]
        vals.append(str(val))

    result += int(str(vals[argmin(positions)]) + str(vals[argmax(positions)]))

file.close()

print(result)
