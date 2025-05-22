for i in [1,2,3,4,5,6,7,8,9,10]:
   
    print(i)

#range(시작,종료,증감치) 시작값부터 시작해서 종료값-1 까지 증감치를 가지고 생성해낸다.
for i in range (1,11) :
    print(i)
a = list(range(1,11))

for kk in range (100, 0,-1):
    print(kk, end=' ')
print()


# # 문제1. 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ...

# for i in range(1, 101):
#     print(i, end=' ')
#     if i % 10 == 0:
#         print()  # 줄 바꿈

# #문자의 유니코드 --> ord
# print( ord('A'))
# print( ord('Z'))
# print( ord('0'))
# print( ord('禁'))

# #코드값 -> 문자로 chr(코드값)
# print (chr(65))

# for i in range(65,91):
#     print(chr(i) , end=" ")

#키보드로 부터 문장을 입력받아서 각문자의 갯수
#  A ===> 5