f = open("10.txt", "r", encoding='UTF-8')
total = 0
lines = f.readline()
for line in lines:
    if "\n" in line:
      line = line[:len(line)-1]
    total += int(line)
print(lines)
f.close()

print("평균", total/len(lines))