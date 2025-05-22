#정수를 하나 입력받아서 양수일 경우에 본래의 값에 *5를 해서 출력해라

n = int(input("정수 : "))
if  n > 0 :
    n = n*5
    print(n)
else :
    print("양의 정수를 입력해주세요")

if n > 0 :
    print("양수입니다")

else :
    print("양수아님 ")
# 양수 0 음수
if n > 0:
    print("양수")

elif n == 0:
    print("0입니다")

else :
    print("음수")

