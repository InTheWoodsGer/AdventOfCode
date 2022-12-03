with open("input.txt") as f:
    lines = f.read().splitlines()

points = 0

for line in lines:
    compartments_1 = line[:len(line) // 2]
    compartments_2 = line[len(line) // 2:]

    for i in range(len(compartments_1)):
        if compartments_1[i:i + 1] in compartments_2:
            ascii_code = ord(compartments_1[i:i + 1])
            points += (ascii_code - (38 if ascii_code < 91 else 96))
            break

print(points)
