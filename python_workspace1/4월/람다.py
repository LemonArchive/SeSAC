# #람다는 한줄짜리 함수, 함수를 쓰고 버린다. 
# def add(x=0,y=0,z=0): #함수는 그 자체가 주소이다 
#     return x+y+z  

# myadd = add #myadd라는 변수에 add함수 주소가 들어간다 
# print( myadd(3,4,5) )

# #함수의 매개변수로 함수를 줄 수 있다. 

# def myfunc(x, y, callback): #세번째인자가 callback - 함수주소를 받아옴 
#     result = callback(x, y)
#     print( x, y, result)

# def add(x,y):
#     return x+y 

# myfunc(4,5, add) #함수주소를 전달한다 
# myfunc(4,5, lambda x, y: x-y) #임시함수를 만든다. lambda로 시작해야 하고 이름은 
# #없으며 두개의 매개변수를 가져야 한다. : 콜론뒤에는 함수의 내용을 기술하면 되고 return 은 생략이다

# fucList = [ lambda x, y : x+y, 
#             lambda x, y : x-y,
#             lambda x, y : x*y,
#             lambda x, y : x/y]
# for fun in fucList:
#     print( fun(9,7))

# #앞에함수, 두번째인자에 iterable이 온다. 
# #특정 조건에 맞는 데이터의 iterable타입을 반환한다. 

a = [1,2,3,4,5,6,7,8,9,10]
# #첫번째 매개변수로 올 함수를 호출하는 호출자는 filter 임 
# #매개변수가 하나이어야 하고, 반환값을 bool타입 True 또는 False이어야 함 
# def isEven(n):
#     return n%2==0

# for i in filter( isEven, a):
#     print(i)


# for i in filter( lambda x:x%2==0, a):
#     print(i)

personList = [
    {"name": '홍길동' , "age": 34, "phone" : '010-0000-0001'},
    {"name": '강감찬' , "age": 74, "phone" : '010-0000-0004'},
    {"name": '서희'   , "age": 54, "phone" : '010-0000-0005'},
    {"name": '윤관'   , "age": 39, "phone" : '010-0000-0003'},
    {"name": '김종서' , "age": 38, "phone" : '010-0000-0006'},
    {"name": '이순신' , "age": 64, "phone" : '010-0000-0002'},
    {"name": '곽재우' , "age": 24, "phone" : '010-0000-0001'}
 ]
#이름이 서희인 사람의 자료를 갖고 오고자 한다.
#filter personList 를 가져갔으니 람다의 매개변수도 personList안의 dict객채
#반환값도 dict객체임
keyname = "서희"
for person in filter(lambda e: e["name"] == keyname, personList):
    print(f"{person['name']} {person['age']} {person['phone']}")

findList = (list(filter(lambda e:e["name"]==keyname, personList)))
print(findList)
#40세 이상만
for person in filter (lambda e : e["age"] >= 40 , personList):
    print(f"{person['name']} {person['age']}{person}['phone'])")

#map, sort : 정령 , zip : 다른언어에 없음
#map - 연산을 수행한다. 나이-5
#첫번째 매개 변수가 매개 변수 하나 값 하나를 반환하는 함수여야한다.
for i in map(lambda x: x*10 , a):
    print(i)

def myfunc2(x):
    x["age"] =x["age"] +5 
for per in map(myfunc2, personList):
    print(per)


#데이터정렬 list타입 자체가 sort메서드가 있다.
#sorted 함수가 filter처럼 별도로 존재한다.
#key라는 매개변수에 람다를 전달해야한다.
a = [9,4,5,6,7,8,1,2,10,3]
a.sort()
print(a)
#dict 타입은 < 연산자가 없다. 에러발생
#람다 매개변수 하나고 반환값이 > 연산자가 지원되는 반환타입만 가능하다.
#오름차순이 기본값이다.

personList.sort(key= lambda x : x ["name"]) #정렬을할때 a[0] < a[1]
print(personList)
personList.sort(key= lambda x : x ["name"], reverse=True ) #reverse값이 False로 되어있다.
print(personList)


#list타입에 속한 함수 sort는 자신의 순서가 바뀐다.
#sorted(iterable데이터, key , reverse) 첫번째 매개변수로 전달된 데이터 원래순서는 안바꾸고
#바뀐 순서를 list로 만들어 정렬한다. 
# 
a = [9,4,5,6,7,8,1,2,10,3]
b = sorted(a)
print("a=", a)
print("b=", b)

personList = [
    {"name": '홍길동' , "age": 34, "phone" : '010-0000-0001'},
    {"name": '강감찬' , "age": 74, "phone" : '010-0000-0004'},
    {"name": '서희'   , "age": 54, "phone" : '010-0000-0005'},
    {"name": '윤관'   , "age": 39, "phone" : '010-0000-0003'},
    {"name": '김종서' , "age": 38, "phone" : '010-0000-0006'},
    {"name": '이순신' , "age": 64, "phone" : '010-0000-0002'},
    {"name": '곽재우' , "age": 24, "phone" : '010-0000-0001'}
 ]

list2 = sorted(personList, key=lambda per:per["name"])
print(list2)

#오늘의 과제
#words= ["assembly", "java","rain","notebook","north","south","hospital",program