import random

class Rock_paper_scissors:

    def __init__(self):
        self.titles = ["", "가위", "바위", "보"]
        self.titles2 = ["", "컴퓨터승", "사람승", "무승부"]
        self.gameList = []

    def gameStart(self):

        while True:
            computer = random.randint(1,3)
            person = int(input("1.가위 2.바위 3. 보"))
            winner = self.isWinner(computer, person)
            print("컴퓨터: ", self.titles[computer],"사람: ",self.titles[person], self.titles2[winner])
            self.gameList.append({"computer": computer, "person": person, "winner": winner})
            again = input("게임을 계속 하시겠습니까? y/n ")
            if again.lower()!=  "y":
                return

       
    def isWinner(self, computer, person):
        if computer == person : # 사람하고 컴퓨터가 같다.
            return 3 # 무승부
        
        elif  (computer == 1 and person == 3) or \
              (computer == 2 and person == 1) or \
              (computer == 3 and person == 2):
                return 1 
        
        return 2 
    
    def gameStatistic(self):
        for game in self.gameList:
            print(f"컴퓨터:{self.titles[game['computer']]}", end="\t")   
            print(f"사람:{self.titles[game['person']]}", end="\t")       
            print(f"승패:{self.titles2[game['winner']]}")                
 
    def output(self):
        print("통계")
        self.gameStatistic()

class Main:
    rps = Rock_paper_scissors()
 
    def gameMain(self):
        while True:
            print("1. 게임시작")            
            print("2. 게임통계")        
            print("3. 게임종료")
            sel = input("선택:" )
            if sel == "1":
                self.rps.gameStart()
            elif sel == "2":
                self.rps.gameStatistic()
            elif sel == "3":
                print("게임을 종료합니다.")
                return

if __name__ =="__main__":
            
    m = Main()
    m.gameMain()


