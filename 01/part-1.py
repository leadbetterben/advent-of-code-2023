file = open("01/input.txt", "r")
result = 0

for line in file.readlines():
    line = line.rstrip("\n")
    digits = [c for i, c in enumerate(line) if c.isdigit()] # Get all digits in line
    val = str(digits[0]) + str(digits[len(digits)-1]) # Append last digit to first
    result += int(val)

file.close()
print(result)
