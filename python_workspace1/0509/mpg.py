f = open("mpg.csv", "r" , encoding='UTF-8')
my_list = []
cy8 = 0
cy6 = 0
cy5 = 0
cy4 = 0
cy3 = 0
cy = 0
while True: # 데이터 한줄읽고 쪼개고 추가
    lines = f.readline().strip()
    if len(lines) == 0 :
        break 
    result = lines.split(',')
    my_list.append(result)


for value in my_list[1:]:

    # mpg += float(value[0])
    cy = int(value[1])
    # disp += float(value[2])
    # hp += float(value[3])
    # weight += float(value[4])
    # accel += float(value[5])
    # model += int(value[6])
    # origin = (value[7])
    # name = (value[8])

    if cy == 8: #cy n개으 실린더
        cy8 += 1 #cy8 실린더갯수8
    elif cy == 6:
        cy6 += 1
    elif cy == 5:
        cy5 += 1
    elif cy == 4:
        cy4 += 1    
    elif cy == 3:
        cy3 += 1

print (f"8기통은 {cy8}개  6기통은 {cy6}개 5기통은 {cy5} 4기통은 {cy4} 3기통은 {cy3}개 입니다.")




    
