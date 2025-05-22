# 가위바위보 게임한판 - computer, person, 승부여부
import random

class GameData:
    #변수선언은 생성자에서 하자 : 이유, 그래야 객체가 생성될떄마다
    #새로운 메모리를 만들어준다.
    def __init__(self):
        self.titles = ["", "가위", "바위", "보"]
        self.titles2 = ["", "컴퓨터 승", "사람 승", "무승부"]
        self.computer = 0
        self.person   = 0
        self.winner   = 0
    
    def gameStart(self):
        self.computer = random.randint(1, 3)
        self.person   = int(input("1. 가위 2.바위 3. 보"))
        self.winner   = self.isWinner()

    def isWinner(self):
        if self.computer == self.person:
            return 3 #무승부
        
        elif (self.computer == 1 and self.person == 3) or \
             (self.computer == 2 and self.person == 1) or \
             (self.computer == 3 and self.person == 2):
            return 1  #패배
        
        else: return 2 # 승리
    
    def printlog(self):
        print(f"컴퓨터의 선택: {self.titles[self.computer]} 사람: {self.titles[self.person]} 승자 {self.titles2[self.winner]}")

if __name__ == "__main__":
    g = GameData()
    g.gameStart()
    g.printlog()



        
    

    
        