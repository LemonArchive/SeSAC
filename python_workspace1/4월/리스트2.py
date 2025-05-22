a = [1,2,3,4]
b = [5,6,7,8]

#리스트를 결합하는 방법, 원본을 안바꾸고 더해진 새로운 listㄹ르 반환
c = a + b # 연산자 중복기능 -> 우리가 연산자를 새로 만들수 있다.

print(c)

a.extend(b) #원본에 추가
print(a)

s = "hello"

if s == "hello" : # if s.equals("hello") -- java
    print("같다")
else :
    print("다르다")

#요소삭제 del 삭제할요소

del c[0]
print(c)


del c[4:] #4번방 이후로 모두 삭제 

print(c)

a = [4,3,5,7,8,1,11,17,12,15,8]

a.sort() # 정렬 :  순서대로 데이터를 배치하는것을 말한다. 
print(a)
         # 오른차순 :  갈수록 커지는거
a.reverse()# 내림차순 :  갈수록 작아지는거
print(a)

#insert - 특정위치에 데이터 추가
a.insert(0, 100)#0번째 위치에 값 100 넣기
print(a)
a.insert(5, 77)#5번쨰위치엑 77
print(a)
a.insert(len(a), 88) #append 함수와 같은 역할을 한다
print(a)

#a.remove  리스트에서 (여러개일떄는 첫번쨰로) 나오는 x를 삭제하는 함수이다.
a.remove(77)
print(a)


#pop함수 pop함수 필요했는지
#컴퓨터안에 데이터를 저장하는구조가 많다.
#배열구조
#링크드리스트 구조

# 스택 구조 - 후입선출(last in first out)
# 큐 구조 - 선입선출(first in first out)
bc = a.pop(1) # 리스트에서 특정값을뽑아 다른변수에할당

print(bc, a)

a=[]
a.insert(0,"A")
a.insert(0,"B")
a.insert(0,"C")
a.insert(0,"D")
a.insert(0,"E")

print(a , type(a))

