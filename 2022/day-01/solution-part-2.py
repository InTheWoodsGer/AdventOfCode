with open("input.txt") as f:
    lines = f.read().splitlines()

elf = 0
calories = [0]

for line in lines:
    if line == "":
        elf += 1
        calories.append(0)
    else:
        calories[elf] += int(line)

calories.sort(reverse=True)
print(calories[0] + calories[1] + calories[2])
