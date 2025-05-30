class MyType:
    # def __init__(self, x,y):
    #     self.x=x
    #     self.y=y
    #연산자중복 = 이미 정해져 있음, 이름이 정해져있고
    #반환형태와 매개변수도 정해져 있다.
    #m3 = m1 +m2
    # m1.__add__(m2)
    # result = m2 + m1
    # m2.__add__(m1)
    #self - 클래스 메서드들은 객체 자신에 대한 참ㅁ조로 누구나
    #self 를 가져야한다. other전달 받은 매개변수
    #반환값이 객체여야 한다.

    def __add__(self, other):

        # print("*********************")
        result = MyType()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result
    def __str__(self):
        print(f"x:{self.x} y:{self.y}")
        #print (객체)

    def __sub__(self):
        pass
m1 = MyType(4,5)
m2 = MyType(8,9)
# m3 = m1 + m2
m3 = m1.__add__(m2)
m3 = m1 + m2
