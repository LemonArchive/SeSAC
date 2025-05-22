f = open("score.txt", "r" , encoding='UTF-8')
stu_list = []
while True:
    
    lines = f.readline().strip()

    if len(lines) == 0 :
        break

    result = lines.split(',')
    stu_list.append(result)
    
for student in stu_list:
    name = student[0]
    kor = int(student[1])
    eng = int(student[2])
    mat = int(student[3])ㄴ
    
    total_score = kor + eng + mat
    avg = (kor + eng + mat) / 3  
    print(f"이름 : 국어 : {kor} 영어 : {eng} 수학 : {mat}\
           총점: {total_score} 평균: {avg:.2f}")

f.close()
