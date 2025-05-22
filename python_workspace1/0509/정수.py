f = open("10.txt", "r")
sum = 0
lines = f.readlines()
for i in range(0,len(lines)):
    sum += int(lines[i])

avg = sum / len(lines)

print(avg)
f.close()