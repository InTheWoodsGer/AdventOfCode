with open("input-test.txt") as f:
    lines = f.read().splitlines()

for code in lines:
    for i in range(len(code)):
        if len(set(code[i:i+14])) == 14:
            print(i + 14)
            break
