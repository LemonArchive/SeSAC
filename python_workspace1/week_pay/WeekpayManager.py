#모듈 Weekpay.py 파일에 있는 클래스 Weekpay 를 가져오겠다.
#외부파일(모듈을) 이 파일로 불러오기 
import pickle

class WeekPayManager:
    
    def __init__(self):
        self.wList = [
            # Weekpay("홍길동", 20, 20000), 
            # Weekpay("고길동", 10, 50000),
            # Weekpay("김길동", 30, 40000),
            # Weekpay("이길동", 40, 20000),
            # Weekpay("장길동", 20, 20000)
        ] #불러오기 테스트를위한 리스트 주석처리

    def output(self):
        for i in self.wList:                
                        
            pay = i.work_time * i.per_pay
            bonus = ((i.work_time - 20) * 1.5) * i.per_pay
            total = pay + bonus
            if i.work_time >= 20: 
                print(f"{i.name}님의 근무시간은 {i.work_time} 시급은 {i.per_pay} 보너스는 {bonus} 총 급여는 {total}입니다")

            else:
                print(f"{i.name}님의 근무시간은 {i.work_time} 시급은 {i.per_pay} 총 급여는 {i.pay}입니다")

    def search(self):
        name = input("찾을이름 : ")
        resultList = list(filter( lambda w : name in w.name, self.wList))
        if len(resultList) == 0:
            print("데이터가 없습니다")
            return 
        
        #resultList[0].output() #Weekpay의 output
        for w in resultList:
            w.output()

    def modify(self):
        name = input("찾을이름 : ")
        resultList = list(filter( lambda w : name in w.name, self.wList))
        if len(resultList) == 0:
            print("데이터가 없습니다")
            return 
        #enumerate함수는 인덱스랑, 데이터를 한꺼번에 반환한다 
        #resultList[0].output() #Weekpay의 output
        for i, w in enumerate(resultList):
            print(i, end ="\t")
            w.output()

        sel = int(input("수정할 대상을 입력하세요(숫자로)"))
        temp = resultList[sel]
        temp.name = input("이름 : ")
        temp.work_time = int(input("근무시간 ")) 
        temp.per_pay = int(input("시간당급여액 ")) 
        temp.process()

    def save(self):
        
        with open ("weekpay.bin", "wb") as f:
            pickle.dump(self.wList, f)

    def load(self):
        
        with open ("weekpay.bin", "rb") as f:
            self.wList = pickle.load(f)
            for i in self.wList:
                
                        
                pay = i.work_time * i.per_pay
                bonus = ((i.work_time - 20) * 1.5) * i.per_pay
                total = pay + bonus
                if i.work_time >= 20: 
                    print(f"{i.name}님의 근무시간은 {i.work_time} 시급은 {i.per_pay} 보너스는 {bonus} 총 급여는 {total}입니다")

                else:
                    print(f"{i.name}님의 근무시간은 {i.work_time} 시급은 {i.per_pay} 총 급여는 {i.pay}입니다")
            


    def menu_display(self):
        print("----------")
        print("   메뉴   ")
        print("----------")
        print("  1.출력  ")
        print("  2.검색  ") #이름
        print("  3.수정  ") #이름
        print("  4.저장  ")
        print("5.불러오기")
        print("  0.종료  ")
        print("----------")      


    def main(self):
        #함수주소를 배열에 저장하고 호출함 , 
        funcList = ["",  self.output, self.search, 
                    self.modify,self.save,self.load]
        while True:
            self.menu_display()
            choice = int(input("선택 : "))
            if choice > 0 and choice < len(funcList):
                funcList[choice]()
            elif choice == 0:
                return
            else :
                print("잘못입력하셨습니다.")

if __name__ =="__main__":
    mgr = WeekPayManager()
    #mgr.output()
    #mgr.search()
    mgr.main()