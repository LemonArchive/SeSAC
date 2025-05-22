class Base: #부모클래스
    def __init__(self, x = 0 ,y = 0):
        self.x = x
        self.y = y
        print("Base 생성자")

    def display(self):
        print( f'x={self.x} y={self.y}') 
    
    def add(self, x, y):
        return self.x+self.y
    
    def doubleX(self):
        return self.x*2
    def doubleY(self):
        return self.y*2
    
#다형성 : overloading  동일 클래스내에서 함수의 이름이 같지만 형태가 다른 함수를 만들 수 있는 성격
#        overriding   성격
#                     def myadd(x, y)  def myadd(x, y, z)
#                     파이썬은 오버로딩을 허용하지 않는다. 대신에
#                     매개변수 기본값이라는 것을 통해서 유사한 결과를 가져온다.
#                     def myadd(x=1, y=2, z=3) myadd(), myadd(10), myadd(10,20) ...
#        overriding - 부모클래스와 자식클래스간에 벌어진다 부모클래스에 있는 메서드가
#                     마음에 안들어서 고쳐쓰기를 원할때, 부모클래스의 함수이름과 자식클래스
#                     함수이름이 같으면 부모의 함수를 가려버린다.
#                     doubleX 특정 변수에 종소고디기떄문에 따로 오버라이딩을 하지않는다.
    

class child1(Base): #Base를 상속받음
    def __init__(self, x = 0, y = 0, z = 0):
        super().__init__(x,y)
        self.z = z
        print("Child1 생성자")

        #다른 언어의 경우에는 부모생성자 먼저 호출하고 자식생성자를 호출 그런데 파이썬은 아님
        #부모생성자를 호출하는 방식으로 설계하는것이 바람직하다.

    def display(self):
        #super(부모클래스의 함수를 먼저 호출하고 내가 만든 코드를 붙이고자 할때)
        #super().함수명()
        print(f"x= {self.x} y= {self.y} z= {self.z}")
        # return super().display()
p = Base(4,9)
c1 = child1(1,2,3)
c1.display()
p.display()

#파이썬은 다중상속을 허용한다.클래스를 동시에 여러개 상속받는 경우
#A -> B -> C 중첩상속 -모든 언어가 이구조는 허용한다.
"""
    A   B
      C    --   부모 클래스가 A,B인경우 두개이상으 클래스를 상속받는 경우를 다중상속이라고 한다.
                다이아몬드상속 

    A -> B  ->D
    A -> C  ->D
                자바는 단일상속만 가능,
"""