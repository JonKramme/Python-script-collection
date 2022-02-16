text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
limit = 30

words = text.split(" ")
lines = [list()]
index = 0
for word in words:
    linelength = len(lines[index])-1
    for x in lines[index]:
        linelength += len(x)
    if linelength + len(word)+1 > limit:
        index += 1
        lines.append(list())
    else:
        lines[index].append(" ")
    lines[index].append(word)

lines[0].pop(0)

for i in range(len(lines)):
    space = limit
    for x in lines[i]:
        space -= len(x)

    while space > 0 and len(lines[i]) > 1:
        for x in range(1, len(lines[i]), 2):
            lines[i][x] = lines[i][x] + " "
            space -= 1
            if space <= 0:
                break

for x in lines:

    print("%s" % "".join(x))
