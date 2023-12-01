a = []
with open("output.txt", "r") as file:
    for line in file.readlines():
        temp = int(line.replace("\n", ""))
        a.append(temp)
print(a)
