# #가변매개변수 -> 함수의 매개변수 개수가 바뀌는 경우에
# print (3,4,5,6,7)
# print (1,2,3)

# def myadd(*args):# 변수하나에 값을 여러개 전달한다.
#     print(type(args))
#     for a in args:
#         print(a)
        
# myadd(1,2)
# myadd(1,2,3)

# def myadd2(*data):
#         s = 0
#         for i in data:
#              s+=i
#         return s
# print(myadd2(1,3,5))
# print(myadd2(1,3,5,7,9))
# print(myadd2(1,3,5,10,12,13))
# #일반인자와 tuple인자를 같이 써야 할때는 일반인자가 먼저 와야 한다.
# #나머지를 tuple로 받으니까

# def myadd3(n, *data):
#      print("n", n)
#      for i in data:
#           print(i)
# myadd3(1,2,3,4,5)
     
# def myfunc(d):
#      print(d)

# person ={"name":"홍길동","age" :12}
# myfunc({"name":"홍길동","age" :12})

# def myfunc2(**d):
#      print(d)

# myfunc2(name="홍길동", age=23)
# #일반인자랑 tuple인자랑 dict인자를 셋다 쓰고 싶으면 순서가 있다.
# #일반인자 , tuple인자 , dict 인자

# def profile(role, *skills, **details):
#      print("Role", role)
#      print("Skills", skills)
#      print("details", details)

# profile("programmer", "python","react","deeplearnin",
#         yearpay=100000000, position="개발자")


#가위바위보 게임
#컴퓨터가 1,2,3 중에 랜덤값 하나를 생각하고 있음
#사람이 1.가위2.바위3.보임 입력받아서 컴퓨터승 사람승 무승부






#컴퓨터의 가위바위보 출력
# crsp = random.randint(1,3)
# print(crsp)


