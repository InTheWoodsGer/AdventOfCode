with open("input.txt") as f:
    lines = f.read().splitlines()

cnt = 0

for line in lines:
    range_1_from = int(line.split(",")[0].split("-")[0])
    range_1_to = int(line.split(",")[0].split("-")[1])
    range_2_from = int(line.split(",")[1].split("-")[0])
    range_2_to = int(line.split(",")[1].split("-")[1])

    if range_1_to >= range_2_from and range_1_from <= range_2_to:
        cnt += 1
    elif range_2_to >= range_1_from and range_2_from <= range_1_to:
        cnt += 1

print(cnt)
