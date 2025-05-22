class Score:
    
    def __init__(self):
        self.scoreList = []
        

    def append(self): #데이터추가함수
        
        score={}    
        score["name"] = input("이름 : ")
        score["kor"] = int(input("국어 : "))
        score["eng"] = int(input("영어 : "))
        score["math"] = int(input("수학 : "))
        score["total"] = int(0)
        score["avg"] = int(0)
        score["grade"] = "미정"
        self.scoreList.append(score) # 목록에 추가하기
        print(f"{score['name']}님의 정보가 추가되었습니다.")
        
    def getTotal(self):
        for score in self.scoreList:
            total = (score["kor"]+score["eng"]+score["math"])
            score["total"] = total

    def getAvg(self):
        for score in self.scoreList:
            avg = score["total"] / 3
            score["avg"] = avg
        

    def getGrade(self):
        print("점수계산이 완료되었습니다")
        for score in self.scoreList:
            if score["avg"]>=90:
                score["grade"] = "수"
            elif score["avg"]>=80:
                score["grade"] = "우"
            elif score["avg"]>=70:
                score["grade"] = "미"
            elif score["avg"]>=60:
                score["grade"] = "양"
            else: score["grade"] = "가"
            
            

    def output(self):
        print(self.scoreList)
        

    def main(self):
        sco = Score()
        while True:
            print ("1.정보추가 2.점수계산 3.점수출력 4.종료" )
            sel = int(input())
            if sel == 1:
                sco.append()
            elif sel == 2: 
                sco.getTotal()       
                sco.getAvg()
                sco.getGrade()
            elif sel == 3:
                sco.output()
            elif sel == 4:
                return


if __name__ == "__main__":

    sco = Score()
    sco.main()

    
    


   