#for문안에서 또 for문이 작동하는경우다
#외부의 루프가 m번 돌고, 내부 루프가 n번돌면  n * m번 수행을 한다
#가급적 2중 for문까지만 동작하게 해야 한다
# for i in range (5):
#     for a in range (5):
#         print(1)
    
#문제1. 이중 for문 사용해서 1~100 까지 출력 단 한줄에 10개씪 출력

#문제2. 이중 for 문

# 1 =
# 1 + 2 = 3 
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10

# for a in range(10):
#     for i in range(1,11):
    
#         print(a * 10 + i , end=' ')
#     print()  # 줄 바꿈



# sum1 = 0
        
# for i in range(1, 11):
#     sum1 = 0  # 각 줄마다 합을 계산하기 위한 변수
#     for j in range(1, i + 1):
#         sum1 += j
#         if j < i:
#             print(j, end=" + ")
#         else:
#             print(j, end=" = ")
#     print(sum1)  # 각 줄의 합 출력


for i in range(1,11,2):#1 3 5 7 9 11
    for j in range (i):
        print("*" , end="")
    print( )   

for i in range (11,0,-2):
    for j in range(i):
        print("*" , end="")
    print( )

