file = open("02/input.txt", "r")
result = 0

for line in file.readlines():
    green = red = blue = 0
    line = line.rstrip("\n")

    # Get game number then drop start of line
    colonPos = line.find(":")
    gameNum = int(line[5: colonPos])
    line = line[colonPos+2:]

    turns = line.split(";")
    for turn in turns:
        cubes = turn.split(",")
        for cube in cubes:
            cube = cube.strip()
            if "blue" in cube:
                blue = max(blue, int(cube[:2]))
            elif "green" in cube:
                green = max(green, int(cube[:2]))
            elif "red" in cube:
                red = max(red, int(cube[:2]))

    result += blue * red * green

file.close()
print(result)
