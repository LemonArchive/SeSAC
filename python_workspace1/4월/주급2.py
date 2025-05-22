
#문제1 주급계산 : 이름 , 근무시간 , 시간당 급여액, 추가수당 : 근무시간이 20시간을 초과하면 
# 추가 시간당 급여액의 50% 가산한다 

# 홍길동 40 10000
# 임꺽정 30 20000
# 장길산 20 20000
# 홍경래 10 15000
# 이징옥 20 30000
nl = []
wtl = []
hrl = []

for i in range(5) :
    name  = input("이름을 입력하세요")

    nl.append(name)

    workTime = int(input("근무시간을 입력해주세요"))

    wtl.append(workTime)

    hourlyRate = int(input("시급을 입력해주세요"))

    hrl.append(hourlyRate)


for i in range(5):

    pay = wtl[i] * hrl[i]
    bonus = pay * 0.5

    if wtl[i] > 20 :
        pay = pay + bonus

        print(f" {nl[i]}님의 총 급여는 {pay} 이며 급여 내 추가수당은 {bonus} 원 입니다.")
    else:
        print(f" {nl[i]}님의 총 급여는 {pay} 원 입니다.")

 
