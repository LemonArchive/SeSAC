# 가위바위보 게임한판 - computer, person, 승부여부
import random

class GameData:
    #변수선언은 생성자에서 하자 : 이유, 그래야 객체가 생성될떄마다
    #새로운 메모리를 만들어준다.
    def __init__(self):
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
    
class Game:
    
    titles = ["", "가위", "바위", "보"]
    titles2 = ["", "컴퓨터승", "사람승", "무승부"]

    def __init__(self):
        self.gameList = []

    def printLog(self, g):
        print(f" 컴퓨터 : {self.titles[g.computer]}", end= "\t") 
        print(f" 사람: {self.titles[g.person]}", end= "\t" )
        print(f" 승자:  {self.titles2[g.winner]}")

 
    def start(self):
        while True:
            g = GameData()
            g.gameStart()
            self.printLog(g)
            self.gameList.append(g)
            
            again = input("1.계속 0.종료?")
            if again != "1":
                return
            
    def printResult(self):
        print(f"{len(self.gameList)}번 수행함")
        for g in self.gameList:
            self.printLog(g)

    def mainStart(self):
        self.start()
        self.printResult()

        
        
if __name__ == "__main__":
    game = Game()
    game.mainStart()
   
    

