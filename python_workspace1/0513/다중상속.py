class Flyable:
    def fly(self):
        print("날 수 있다")
    
    def walk(self):
        print("***두다리로 걷는다***")
        
class Swimmable:
    def swim(self):
        print("수영 할 수 있다.")

class Duck(Flyable,Swimmable):
    def quack(self):
        print("꽥꽥")

d1 = Duck()
d1.fly()
d1.swim()
d1.quack()
d1.walk() #메서드명이 동일한 경우에는 앞에거 먼저 호출한다.
#시스템이 제공하느 내장변수중에 __mro__가 상속받은 관계정보가 있엉서 
#이걸따라서 적용함
print( Duck.__mro__)