import fileinput


lines = []

for line in fileinput.input():
    lines.append(line)


result=int(lines[0])+int(lines[1])
print(str(result))