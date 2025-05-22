import random
strike = 0
ball = 0
out = 0
#입력 : 3개의 숫자
#출력 : 컴퓨터가 생각하는숫자 
# s(정확한숫자 정확한위치) b(정확한숫자 틀린위치) (o 관련없는숫자) 
# 3개의 숫자을 입력받아 컴퓨터가 지정한숫자 3가지와 위치가 모두맞는지
computer = random.sample(range(1,10),3)
print(computer)

a = input()
b = a.split(",")
intb= list(map(int,b))
cb = list(computer)
print(intb)
print(type(intb))
print(cb)
print(type(cb))

for i in range(1,3):
    if intb[i] == cb[ㅑ]:
        strike += 1
    elif intb[i] == cb[1] or intb[i] == cb[2]:
        ball += 1
    else: out += 1
    print(f"{strike} strike {ball} ball {out} out")

    # return

    if strike == 3:
        
        print(f"{strike} strike {ball} ball {out} out")
        print("성공!")


#intb 1과 2 3 을비교해서 같다 = 볼 else out
print(f"{strike} strike {ball} ball {out} out")

