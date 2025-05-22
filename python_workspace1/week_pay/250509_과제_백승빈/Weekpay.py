class Weekpay:

    def __init__(self, name="", work_time=20, per_pay=10000):
        self.name = name
        self.work_time = work_time
        self.per_pay = per_pay
        self.process()#클래스 내부 함수 호출시 self로 해야한다.

    def process(self):
        self.pay = self.work_time * self.per_pay
        self.bonus = (self.work_time - 20) * 0.5
        self.total = self.pay + self.bonus
        
            

    def output(self):
        if self.work_time >= 20: 
            print(f"{self.name}님의 근무시간은 {self.work_time} 시급은 {self.per_pay} 보너스는 {self.bonus} 총 급여는 {self.total}입니다")

        else:
            print(f"{self.name}님의 근무시간은 {self.work_time} 시급은 {self.per_pay} 총 급여는 {self.pay}입니다")
        print(type(self.work_time))
#파이썬의 모듈들은 내장변수가있다.__name__ 
print( __name__)# 이모듈로 직접실행하면 main이 들어온다 python Weekpay.py
#import 되서 실행되면 파일명이 전달됨 python WeekpayManager.py
if __name__ == "__main__":
    w1 = Weekpay("A")
    w1.output()
