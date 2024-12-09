rus = open("RUS.txt", 'r+')
rus2 = open("RUS.txt", 'r+')
lines = rus.readlines()
lines = lines[0].split()
lines2 = rus2.readlines()
lines2 = lines2[0].split()

def Mest(lines, go):
    if go == '': go = '*****'
    for i in range(len(lines)):
        if go[0] == '*':
            break
        if lines[i][0] != go[0]:
            lines[i] = None
    lines = list(filter(None, lines))

    for i in range(len(lines)):
        if go[1] == '*':
            break
        if lines[i][1] != go[1]:
            lines[i] = None
    lines = list(filter(None, lines))

    for i in range(len(lines)):
        if go[2] == '*':
            break
        if lines[i][2] != go[2]:
            lines[i] = None
    lines = list(filter(None, lines))

    for i in range(len(lines)):
        if go[3] == '*':
            break
        if lines[i][3] != go[3]:
            lines[i] = None
    lines = list(filter(None, lines))

    for i in range(len(lines)):
        if go[4] == '*':
            break
        if lines[i][4] != go[4]:
            lines[i] = None
    lines = list(filter(None, lines))

    print(lines)
    return lines


def Iskluch(lines, gid):
    for i in range(len(lines)):
        for o in range(len(gid)):
            if lines[i].find(gid[o]) != -1:
                lines[i] = None
                break
    lines = list(filter(None, lines))
    print(lines)

    return lines


def Izvesn(lines, gid2):
    for i in range(len(lines)):
        for o in range(0, len(gid2), 2):
            if lines[i].find(gid2[o]) == -1:
                lines[i] = None
                break
            elif lines[i][int(gid2[o + 1])] == gid2[o]:
                lines[i] = None
                break
    lines = list(filter(None, lines))
    print(lines)

    return lines

def Zanovo(lines, lines2):
    lines.clear()
    lines = lines2
    return lines
