with open("input.txt") as f:
    lines = f.read().splitlines()

points = 0

for i in range(0, len(lines), 3):
    for base_letter in lines[i]:
        if base_letter in lines[i + 1] and base_letter in lines[i + 2]:
            ascii_code = ord(base_letter)
            points += (ascii_code - (38 if ascii_code < 91 else 96))
            break

print(points)
