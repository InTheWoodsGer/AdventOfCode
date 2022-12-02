with open("input.txt") as f:
    lines = f.read().splitlines()

lines.append("")

max = 0
current = 0
for line in lines:
    if line == "":
        if max < current:
            max = current
        current = 0
    else:
        current += int(line)

print(max)
