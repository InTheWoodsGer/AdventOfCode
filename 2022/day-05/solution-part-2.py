with open("input.txt") as f:
    lines = f.read().splitlines()

stack_cnt = None
stacks = list()
init_phase = True

for line in lines:
    if line[0:2] == " 1":
        init_phase = False
        continue
    elif line == "":
        continue

    if init_phase:
        if not stack_cnt:
            stack_cnt = len(line) // 4 + 1
            for i in range(stack_cnt):
                stacks.append(list())

        for i in range(stack_cnt):
            crate = line[1 + (4 * i):2 + (4 * i)]
            if not crate.isspace():
                stacks[i].append(crate)

    else:
        p_move = int(line.split(" ")[1])
        p_from = int(line.split(" ")[3]) - 1
        p_to = int(line.split(" ")[5]) - 1

        crates_to_move = stacks[p_from][0:p_move]
        stacks[p_from] = stacks[p_from][p_move:]
        stacks[p_to] = crates_to_move + stacks[p_to]

print("".join(stack[0] for stack in stacks))
