# class Person:
#     #이 이공간은 플래스 공간이다. 클래스 정의할때 딱 한번실행된다.
#     #객체 만들떄마다 실행되지않음. 그래서 list 타입이나 dict타입등 함부로 여기에
#     #선언하면 안된다.
#     name = "홍길동"
#     age = 12
#     phone = ["010-0000-0001,010-0000-0002"] # 공통 공간 공통 변수 사용시
#     #생성자에서 변수를 만들자
#     def __init__(self):# 파이썬은 생성자에서 변수를 만든다.
#         self.name = "" 
#         self.age = 0
#         self.phone = []

#     def append(self, name="임꺽정", age=13, phone="010-0000-0003"):
#         self.name = name
#         self.age  = age

#         self.phone.append( phone )
    
#     def output(self):
#         print(self.name, self.age, self.phone)
# p1 = Person()
# p1.append("장길산", 11, "010-0000-0003")

# p2 = Person()
# p2.append("김종서", 13, "010-0000-0004")    

# p1.output()
# p2.output()
# """
# 주급 : 이름, 시간당 급여액 , 근무시간
# """

class Pay:

    def __init__(self, name="임꺽정", perPay=100000, time= 20):
        self.name = ""
        self.perPay = 0
        self.time = 0


    def output(self):
        print(self.name ,"님의 시급은", self.perPay,"근무시간은", self.time ,"총 급여는", self.perPay * self.time ,"입니다")

p1 = Pay()
p1.append("ㅇㅇㅇ", 13000, 50)

print
p1.output()
    