# #외부 모듈을 사용하기
# import mod1 # 파일 전체가 메모리에 로딩된다.
# import mod1 as md # 모듈명이 길경우 aliasing 다른 이름으로 부를 수 있다.
# print(mod1.add(3,4))
# print(mod1.sub(3,4))

# p2 = md.Person("윤하",44)
# p2.print()

# #파일명 쓰기 싫고 마치 내함수 처럼 쓰고싶다~ 하면 
# from mod1 import add, sub

# from mod1 import Person
# p3 = Person("조이", 24)
# p3.print()
# print(add(3,5))
# print(sub(3,5))

# #수학라이브러리 -> 머신러닝의 경우 무조건 numpy타입으로 전환해야 한다
# import numpy as np
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [x*2 for x in a]
# c = a+b

# print(a)
# print(b)
# print(c)

# a1 = np.array(a)
# b1 = 2 * a1
# c1 = a1 + b1
# print(a1)
# print(b1)
# print(c1)

"""
스칼라 연산 - 1:1 연산, ,대부분은 프로그램이 언어가 이걸지원
            다:다 연선안 for 문을 써서 해야 했다.
통계 분석용 언어들은 수학에 가깝게 벡터연산을 지원한다.
벡터연산 - 다대다 연산을 한다. R,python의 numpy,pandas 라이브러리
들이 벡터연산을 지원한다

mymodule2.py 파일명을

isEven(4) #짝수면 True 홀수면 False 반환
toUpper('asterisk') #대문자 반환 -> ASTERISK
"""
import mymodule2 as mm2

print(mm2.isEven(7))
print(mm2.toUpper("shduksahd"))