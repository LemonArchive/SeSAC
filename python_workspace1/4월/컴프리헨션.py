#컴프리헨션
a = [1,2,3,4,5,6,7,8,9,10]
b = a
a[2] = -3
print(a,b)

#스택 하고 합을 시스템이 프로세스한테 할당한다
#스택에는 변수 자신이 저장된다
#힙에는 데이터가 저장된다. 저장된 주소를 변수한테 전달한다
# a(100번지) ==========> (1,2,3,4,5,6,7,8,9,10)

# b = a : 동일한 데이터 공간을 공유한다.
# b라는 메모리 공간을 스택에 만들고 a의 값 (데이터가 있는곳의 주소)
#를 복사한다. 소프트카피, 얖은카피라고 부른다'
#소프트카피의 목적은 메모리 절약, 쓸데없는 복사과정(overhead) 이 필요없다
#하드카피 ,깊은카피의 경우는 직접 구현하거나 deepcopy 모듈을 사용하거나 컴프리헨션을 사용한다

#사용자가 구현한 하드카피 상황
b = [] #새로 기억공간을 만든다 
for item in a : #a로부터 데이터를 하나씩 가져ㅕ와서 item이라는 변수에 저장한다
    b.append(item)
b[3]=99
print(a)
print(b)

#컴프리헨션  :리스트 복사 [변수명 for 변수명 in 리스트형변수]

c = [item for item in a]
c[5] = 55
print("a= ", a)
print("c= ", c)

d = [ item*2 for item in a]
print("d= ", d , type(d))
#조건을 부여할 수도 있다. [변수명 for 변수명 in 리스트형변수    if 변수명> 0]
oddList = [ x for x in a if x%2==1 ]
print(oddList)

wordList = ["rain","desk","hospital","building","java","python","cloud","rainbow","assembly","javascript","html","css"]

wordList2 = [w for w in wordList]
print(wordList2)

#단어와 단어길이
wordList3 = [(w,len(w), w.upper()) for w in wordList]
print(wordList3)

#단어길이가 5글자 이상인것만

wordList3 = [w for w in wordList if len(w)>=5]
print(wordList3)

#문제1. 단어중에 java 라는 단어가 있는거만 추출하기
#문제2. 단어중에 길이가 5개보다 짧은 단어가 있는거만 추출하기

#문제1
wList1 = [w for w in wordList if "java" in w]
print(wList1)

#문제2
wList2 = [w for w in wordList if len(w) < 5]
print(wList2)

