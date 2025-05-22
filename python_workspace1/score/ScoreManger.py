from ScoreData import ScoreData
import pickle

class ScoreManager:
    def __init__(self): #생성자-파이썬에서는 변수도 만들고
                        #첫 시작시 준비작업
        self.scoreList = [
            ScoreData(),
            ScoreData("조승연",90,80,80),
            ScoreData("안세영",100,80,70),
            ScoreData("김연경",70,90,60),
            ScoreData("김연아",90,60,0)
            ]

    def print_all(self):
        for s in self.scoreList:
            s.print()


    def menu_display(self):
        print("----------")
        print("   메뉴   ")
        print("----------")
        print("  1.추가  ")
        print("  2.출력  ")
        print("  3.검색  ") #이름
        print("  4.수정  ") #이름
        print("  5.삭제  ") #이름
        print("  6.정렬  ") #총점 내림차순
        print("  7.저장  ")
        print("8.불러오기")
        print("  0.종료  ")
        print("----------")


    def save(self):
        
        with open ("scoreList.bin", "wb") as f:
            pickle.dump(self.scoreList, f)

    def load(self):
        
        with open ("scoreList.bin", "rb") as f:
            self.scoreList = pickle.load(f)
        self.print_all()


    def append(self):
        sc = ScoreData()
        sc.name = input("이름 : ")
        sc.kor = int(input("국어 : "))
        sc.eng = int(input("영어 : "))
        sc.mat = int(input("수학 : "))
        sc.process()
        self.scoreList.append(sc)

    def output(self):
        print(self.scoreList)

    def search(self):
        
        name = input("찾을 이름 : ")
        result_list = list(filter(lambda w : name == w.name, self.scoreList))
        if len(result_list) == 0:
            print("데이터가 없습니다.")
            return
        
        for w in result_list:
            w.print()

    def modify(self):
        name = input("찾을 이름 : ")
        result_list = list(filter(lambda w : name == w.name, self.scoreList))
        if len(result_list) == 0:
            print("데이터가 없습니다.")
            return
        for w in result_list:
            print(f"{w.name} 의 데이터를 수정합니다.")
            w.kor = int(input("국어 : "))
            w.eng = int(input("영어 : "))
            w.mat = int(input("수학 : "))
            w.process()
            print("수정이 완료되었습니다.")


        
    def delete(self):
        name = input("찾을 이름 : ")
        result_list = list(filter(lambda w : name == w.name, self.scoreList))
        if len(result_list) == 0:
            print("데이터가 없습니다.")
            return
        
        for w in result_list:
            self.scoreList.remove(w)
            print(f"{w.name}님의 데이터 삭제가 완료되었습니다.")

    def sort_desc(self):
        self.scoreList.sort(key = lambda x: x.total, reverse = True)
        print("총점 내림차순으로 정렬되었습니다.")
        

    def main(self):
        #함수주소를 배열에 저장하고 호출함 , 
        funcList = ["", self.append, self.print_all, self.search, 
                    self.modify,self.delete,self.sort_desc,
                    self.save,self.load]
        while True:
            self.menu_display()
            choice = int(input("선택 : "))
            if choice > 0 and choice < len(funcList):
                funcList[choice]()
            elif choice == 0:
                return
            else :
                print("잘못입력하셨습니다.")
            
if __name__ == "__main__":
    sm = ScoreManager()
    sm.main()

